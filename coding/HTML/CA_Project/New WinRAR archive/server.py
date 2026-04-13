"from fastapi import FastAPI, APIRouter, HTTPException, Header, UploadFile, File, Response, Cookie, Query
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
import uuid
from datetime import datetime, timezone, timedelta
import requests
from storage import init_storage, put_object, get_object

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

app = FastAPI()
api_router = APIRouter(prefix=\"/api\")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class User(BaseModel):
    model_config = ConfigDict(extra=\"ignore\")
    user_id: str
    email: str
    name: str
    picture: Optional[str] = None
    role: str = \"client\"
    created_at: str

class Service(BaseModel):
    model_config = ConfigDict(extra=\"ignore\")
    service_id: str
    title: str
    description: str
    icon: Optional[str] = None
    order: int
    is_active: bool = True
    created_at: str

class ServiceCreate(BaseModel):
    title: str
    description: str
    icon: Optional[str] = None
    order: Optional[int] = 0

class ServiceUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    order: Optional[int] = None
    is_active: Optional[bool] = None

class Submission(BaseModel):
    model_config = ConfigDict(extra=\"ignore\")
    submission_id: str
    client_user_id: str
    client_name: str
    client_email: str
    dob: Optional[str] = None
    gender: Optional[str] = None
    additional_info: Optional[str] = None
    document_path: Optional[str] = None
    original_filename: Optional[str] = None
    submitted_at: str

class SubmissionCreate(BaseModel):
    client_name: str
    client_email: str
    dob: Optional[str] = None
    gender: Optional[str] = None
    additional_info: Optional[str] = None

class SessionRequest(BaseModel):
    session_id: str

async def get_current_user(authorization: str = Header(None), session_token: str = Cookie(None)) -> dict:
    \"\"\"Extract user from session_token (cookie first, then header fallback)\"\"\"
    token = session_token or (authorization.replace(\"Bearer \", \"\") if authorization else None)
    
    if not token:
        raise HTTPException(status_code=401, detail=\"Not authenticated\")
    
    session_doc = await db.user_sessions.find_one({\"session_token\": token}, {\"_id\": 0})
    if not session_doc:
        raise HTTPException(status_code=401, detail=\"Invalid session\")
    
    expires_at = session_doc[\"expires_at\"]
    if isinstance(expires_at, str):
        expires_at = datetime.fromisoformat(expires_at)
    if expires_at.tzinfo is None:
        expires_at = expires_at.replace(tzinfo=timezone.utc)
    
    if expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=401, detail=\"Session expired\")
    
    user_doc = await db.users.find_one({\"user_id\": session_doc[\"user_id\"]}, {\"_id\": 0})
    if not user_doc:
        raise HTTPException(status_code=401, detail=\"User not found\")
    
    return user_doc

async def require_admin(authorization: str = Header(None), session_token: str = Cookie(None)) -> dict:
    \"\"\"Require admin role\"\"\"
    user = await get_current_user(authorization, session_token)
    if user.get(\"role\") != \"admin\":
        raise HTTPException(status_code=403, detail=\"Admin access required\")
    return user

@api_router.post(\"/auth/session\")
async def exchange_session(request: SessionRequest):
    \"\"\"Exchange session_id for user data and session_token.
    REMINDER: DO NOT HARDCODE THE URL, OR ADD ANY FALLBACKS OR REDIRECT URLS, THIS BREAKS THE AUTH\"\"\"
    try:
        resp = requests.get(
            \"https://demobackend.emergentagent.com/auth/v1/env/oauth/session-data\",
            headers={\"X-Session-ID\": request.session_id},
            timeout=10
        )
        resp.raise_for_status()
        session_data = resp.json()
        
        user_id = f\"user_{uuid.uuid4().hex[:12]}\"
        existing_user = await db.users.find_one({\"email\": session_data[\"email\"]}, {\"_id\": 0})
        
        if existing_user:
            user_id = existing_user[\"user_id\"]
            await db.users.update_one(
                {\"user_id\": user_id},
                {\"$set\": {
                    \"name\": session_data.get(\"name\", existing_user.get(\"name\")),
                    \"picture\": session_data.get(\"picture\", existing_user.get(\"picture\"))
                }}
            )
        else:
            await db.users.insert_one({
                \"user_id\": user_id,
                \"email\": session_data[\"email\"],
                \"name\": session_data.get(\"name\", \"\"),
                \"picture\": session_data.get(\"picture\"),
                \"role\": \"client\",
                \"created_at\": datetime.now(timezone.utc).isoformat()
            })
        
        session_token = session_data[\"session_token\"]
        expires_at = datetime.now(timezone.utc) + timedelta(days=7)
        
        await db.user_sessions.insert_one({
            \"user_id\": user_id,
            \"session_token\": session_token,
            \"expires_at\": expires_at.isoformat(),
            \"created_at\": datetime.now(timezone.utc).isoformat()
        })
        
        user_doc = await db.users.find_one({\"user_id\": user_id}, {\"_id\": 0})
        
        response = JSONResponse(content={\"user\": user_doc})
        response.set_cookie(
            key=\"session_token\",
            value=session_token,
            httponly=True,
            secure=True,
            samesite=\"none\",
            path=\"/\",
            max_age=7*24*60*60
        )
        return response
    except Exception as e:
        logger.error(f\"Session exchange failed: {e}\")
        raise HTTPException(status_code=400, detail=str(e))

@api_router.get(\"/auth/me\")
async def get_me(authorization: str = Header(None), session_token: str = Cookie(None)):
    \"\"\"Get current user\"\"\"
    user = await get_current_user(authorization, session_token)
    return user

@api_router.post(\"/auth/logout\")
async def logout(authorization: str = Header(None), session_token: str = Cookie(None)):
    \"\"\"Logout user\"\"\"
    user = await get_current_user(authorization, session_token)
    token = session_token or (authorization.replace(\"Bearer \", \"\") if authorization else None)
    await db.user_sessions.delete_one({\"session_token\": token})
    
    response = JSONResponse(content={\"message\": \"Logged out\"})
    response.delete_cookie(key=\"session_token\", path=\"/\", samesite=\"none\", secure=True)
    return response

@api_router.get(\"/services\", response_model=List[Service])
async def get_services():
    \"\"\"Get all active services (public)\"\"\"
    services = await db.services.find({\"is_active\": True}, {\"_id\": 0}).sort(\"order\", 1).to_list(1000)
    for service in services:
        if isinstance(service.get(\"created_at\"), str):
            pass
        else:
            service[\"created_at\"] = service.get(\"created_at\", datetime.now(timezone.utc)).isoformat()
    return services

@api_router.post(\"/submissions\")
async def create_submission(
    submission: SubmissionCreate,
    file: Optional[UploadFile] = File(None),
    authorization: str = Header(None),
    session_token: str = Cookie(None)
):
    \"\"\"Create client submission with optional document upload\"\"\"
    user = await get_current_user(authorization, session_token)
    
    submission_id = f\"sub_{uuid.uuid4().hex[:12]}\"
    document_path = None
    original_filename = None
    
    if file:
        ext = file.filename.split(\".\")[-1] if \".\" in file.filename else \"bin\"
        path = f\"giriasocc/uploads/{user['user_id']}/{uuid.uuid4()}.{ext}\"
        data = await file.read()
        
        result = put_object(path, data, file.content_type or \"application/octet-stream\")
        document_path = result[\"path\"]
        original_filename = file.filename
        
        await db.files.insert_one({
            \"file_id\": f\"file_{uuid.uuid4().hex[:12]}\",
            \"storage_path\": document_path,
            \"original_filename\": original_filename,
            \"content_type\": file.content_type,
            \"size\": result[\"size\"],
            \"user_id\": user[\"user_id\"],
            \"is_deleted\": False,
            \"created_at\": datetime.now(timezone.utc).isoformat()
        })
    
    submission_doc = {
        \"submission_id\": submission_id,
        \"client_user_id\": user[\"user_id\"],
        \"client_name\": submission.client_name,
        \"client_email\": submission.client_email,
        \"dob\": submission.dob,
        \"gender\": submission.gender,
        \"additional_info\": submission.additional_info,
        \"document_path\": document_path,
        \"original_filename\": original_filename,
        \"submitted_at\": datetime.now(timezone.utc).isoformat()
    }
    
    await db.submissions.insert_one(submission_doc)
    return submission_doc

@api_router.get(\"/submissions/my\", response_model=List[Submission])
async def get_my_submissions(authorization: str = Header(None), session_token: str = Cookie(None)):
    \"\"\"Get current user's submissions\"\"\"
    user = await get_current_user(authorization, session_token)
    submissions = await db.submissions.find(
        {\"client_user_id\": user[\"user_id\"]},
        {\"_id\": 0}
    ).sort(\"submitted_at\", -1).to_list(1000)
    return submissions

@api_router.get(\"/admin/submissions\", response_model=List[Submission])
async def get_all_submissions(authorization: str = Header(None), session_token: str = Cookie(None)):
    \"\"\"Get all submissions (admin only)\"\"\"
    await require_admin(authorization, session_token)
    submissions = await db.submissions.find({}, {\"_id\": 0}).sort(\"submitted_at\", -1).to_list(1000)
    return submissions

@api_router.get(\"/admin/services\", response_model=List[Service])
async def admin_get_services(authorization: str = Header(None), session_token: str = Cookie(None)):
    \"\"\"Get all services including inactive (admin only)\"\"\"
    await require_admin(authorization, session_token)
    services = await db.services.find({}, {\"_id\": 0}).sort(\"order\", 1).to_list(1000)
    return services

@api_router.post(\"/admin/services\", response_model=Service)
async def create_service(
    service: ServiceCreate,
    authorization: str = Header(None),
    session_token: str = Cookie(None)
):
    \"\"\"Create service (admin only)\"\"\"
    await require_admin(authorization, session_token)
    
    service_id = f\"svc_{uuid.uuid4().hex[:12]}\"
    service_doc = {
        \"service_id\": service_id,
        \"title\": service.title,
        \"description\": service.description,
        \"icon\": service.icon,
        \"order\": service.order,
        \"is_active\": True,
        \"created_at\": datetime.now(timezone.utc).isoformat()
    }
    
    await db.services.insert_one(service_doc)
    return service_doc

@api_router.put(\"/admin/services/{service_id}\", response_model=Service)
async def update_service(
    service_id: str,
    updates: ServiceUpdate,
    authorization: str = Header(None),
    session_token: str = Cookie(None)
):
    \"\"\"Update service (admin only)\"\"\"
    await require_admin(authorization, session_token)
    
    update_data = {k: v for k, v in updates.model_dump().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail=\"No updates provided\")
    
    result = await db.services.update_one(
        {\"service_id\": service_id},
        {\"$set\": update_data}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail=\"Service not found\")
    
    service_doc = await db.services.find_one({\"service_id\": service_id}, {\"_id\": 0})
    return service_doc

@api_router.delete(\"/admin/services/{service_id}\")
async def delete_service(
    service_id: str,
    authorization: str = Header(None),
    session_token: str = Cookie(None)
):
    \"\"\"Delete service (admin only)\"\"\"
    await require_admin(authorization, session_token)
    
    result = await db.services.delete_one({\"service_id\": service_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=\"Service not found\")
    
    return {\"message\": \"Service deleted\"}

@api_router.get(\"/files/{path:path}\")
async def download_file(
    path: str,
    authorization: str = Header(None),
    session_token: str = Cookie(None),
    auth: str = Query(None)
):
    \"\"\"Download file (auth required)\"\"\"
    auth_header = authorization or (f\"Bearer {auth}\" if auth else None)
    await get_current_user(auth_header, session_token)
    
    record = await db.files.find_one({\"storage_path\": path, \"is_deleted\": False}, {\"_id\": 0})
    if not record:
        raise HTTPException(status_code=404, detail=\"File not found\")
    
    try:
        data, content_type = get_object(path)
        return Response(
            content=data,
            media_type=record.get(\"content_type\", content_type),
            headers={
                \"Content-Disposition\": f'inline; filename=\"{record.get(\"original_filename\", \"download\")}\"'
            }
        )
    except Exception as e:
        logger.error(f\"File download failed: {e}\")
        raise HTTPException(status_code=500, detail=\"File download failed\")

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=[\"*\"],
    allow_headers=[\"*\"],
)

@app.on_event(\"startup\")
async def startup():
    \"\"\"Initialize storage and seed default services\"\"\"
    try:
        init_storage()
        logger.info(\"Storage initialized\")
        
        count = await db.services.count_documents({})
        if count == 0:
            default_services = [
                {
                    \"service_id\": f\"svc_{uuid.uuid4().hex[:12]}\",
                    \"title\": \"GST & Tax Filing\",
                    \"description\": \"Comprehensive GST registration, filing, and compliance services for businesses of all sizes.\",
                    \"icon\": \"receipt\",
                    \"order\": 1,
                    \"is_active\": True,
                    \"created_at\": datetime.now(timezone.utc).isoformat()
                },
                {
                    \"service_id\": f\"svc_{uuid.uuid4().hex[:12]}\",
                    \"title\": \"Audit & Assurance\",
                    \"description\": \"Professional audit services ensuring financial accuracy and regulatory compliance.\",
                    \"icon\": \"shield-check\",
                    \"order\": 2,
                    \"is_active\": True,
                    \"created_at\": datetime.now(timezone.utc).isoformat()
                },
                {
                    \"service_id\": f\"svc_{uuid.uuid4().hex[:12]}\",
                    \"title\": \"Business Advisory\",
                    \"description\": \"Strategic financial planning and advisory services to optimize your business growth.\",
                    \"icon\": \"chart-line-up\",
                    \"order\": 3,
                    \"is_active\": True,
                    \"created_at\": datetime.now(timezone.utc).isoformat()
                },
                {
                    \"service_id\": f\"svc_{uuid.uuid4().hex[:12]}\",
                    \"title\": \"Company Incorporation\",
                    \"description\": \"End-to-end company registration and incorporation services with legal compliance.\",
                    \"icon\": \"briefcase\",
                    \"order\": 4,
                    \"is_active\": True,
                    \"created_at\": datetime.now(timezone.utc).isoformat()
                },
                {
                    \"service_id\": f\"svc_{uuid.uuid4().hex[:12]}\",
                    \"title\": \"Accounting Services\",
                    \"description\": \"Complete bookkeeping and accounting solutions for accurate financial records.\",
                    \"icon\": \"calculator\",
                    \"order\": 5,
                    \"is_active\": True,
                    \"created_at\": datetime.now(timezone.utc).isoformat()
                }
            ]
            await db.services.insert_many(default_services)
            logger.info(\"Default services seeded\")
    except Exception as e:
        logger.error(f\"Startup failed: {e}\")

@app.on_event(\"shutdown\")
async def shutdown_db_client():
    client.close()
"
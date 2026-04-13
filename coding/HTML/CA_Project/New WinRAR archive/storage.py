"import os
import requests
import logging

logger = logging.getLogger(__name__)
STORAGE_URL = \"https://integrations.emergentagent.com/objstore/api/v1/storage\"
APP_NAME = \"giriasocc\"
storage_key = None

def init_storage():
    \"\"\"Initialize storage and return storage_key. Call once at startup.\"\"\"
    global storage_key
    if storage_key:
        return storage_key
    
    emergent_key = os.environ.get(\"EMERGENT_LLM_KEY\")
    if not emergent_key:
        raise ValueError(\"EMERGENT_LLM_KEY not found in environment\")
    
    try:
        resp = requests.post(
            f\"{STORAGE_URL}/init\",
            json={\"emergent_key\": emergent_key},
            timeout=30
        )
        resp.raise_for_status()
        storage_key = resp.json()[\"storage_key\"]
        logger.info(\"Storage initialized successfully\")
        return storage_key
    except Exception as e:
        logger.error(f\"Storage init failed: {e}\")
        raise

def put_object(path: str, data: bytes, content_type: str) -> dict:
    \"\"\"Upload file. Returns {\"path\": \"...\", \"size\": 123, \"etag\": \"...\"}\"\"\"
    key = init_storage()
    resp = requests.put(
        f\"{STORAGE_URL}/objects/{path}\",
        headers={\"X-Storage-Key\": key, \"Content-Type\": content_type},
        data=data,
        timeout=120
    )
    resp.raise_for_status()
    return resp.json()

def get_object(path: str) -> tuple[bytes, str]:
    \"\"\"Download file. Returns (content_bytes, content_type).\"\"\"
    key = init_storage()
    resp = requests.get(
        f\"{STORAGE_URL}/objects/{path}\",
        headers={\"X-Storage-Key\": key},
        timeout=60
    )
    resp.raise_for_status()
    return resp.content, resp.headers.get(\"Content-Type\", \"application/octet-stream\")
"
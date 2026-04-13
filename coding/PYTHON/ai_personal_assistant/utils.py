from dotenv import load_dotenv
import os

load_dotenv()

def get_env_variable(var_name: str, default: Optional[str] = None):
    return os.getenv(var_name, default)

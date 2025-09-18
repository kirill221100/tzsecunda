from fastapi import HTTPException, Security
from fastapi import status
from fastapi.security import api_key
from src.config import cfg

api_key_header = api_key.APIKeyHeader(name="X-API-KEY")

async def require_api_key(key: str = Security(api_key_header)):
    if key != cfg.API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")


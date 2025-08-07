
import firebase_admin
from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin import credentials, auth
from app.core.config import settings

cred = credentials.Certificate(settings.FIREBASE_CERT_PATH)
firebase_admin.initialize_app(cred)

security = HTTPBearer()

def get_current_user(http_cred: HTTPAuthorizationCredentials = Depends(security)):
    token = http_cred.credentials
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
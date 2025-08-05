from fastapi import FastAPI
from app.api.routes.routes_user import router as user_router
from app.db.session import engine
from app.db.session import Base

app = FastAPI(title="FastAPI")

Base.metadata.create_all(bind=engine)

app.include_router(user_router, prefix="/api/users", tags=["Users"])
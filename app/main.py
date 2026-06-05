from fastapi import FastAPI
from app.api.v1.users import users_router
from app.api.v1.posts import posts_router


app = FastAPI(title="EduTrack API", version="1.0.0")
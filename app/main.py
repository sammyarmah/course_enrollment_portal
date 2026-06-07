from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.auth import router as auth_router
from app.api.v1.user import router as user_router
from app.api.v1.course import router as course_router
from app.api.v1.enrollment import router as enrollment_router


app = FastAPI(title=settings.PROJECT_NAME)


app.include_router(auth_router, prefix=settings.API_V1_PREFIX)
app.include_router(user_router, prefix=settings.API_V1_PREFIX)
app.include_router(course_router, prefix=settings.API_V1_PREFIX)
app.include_router(enrollment_router, prefix=settings.API_V1_PREFIX)
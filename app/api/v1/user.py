from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.deps import get_async_db, get_current_active_user, get_current_admin
from app.schemas.users import UserRead
from app.services.user import UserService


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserRead)
async def get_profile(current_user=Depends(get_current_active_user)):
    return current_user


@router.get("/", response_model=list[UserRead])
async def get_all_users(db: AsyncSession = Depends(get_async_db), admin=Depends(get_current_admin)):
    return await UserService.get_all_users(db)
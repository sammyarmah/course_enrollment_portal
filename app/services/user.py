from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repo import UserRepository


class UserService:

    @staticmethod
    async def get_profile(current_user):
        return current_user

    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: int):
        user = await UserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    async def get_all_users(db: AsyncSession):
        return await UserRepository.get_all(db)

    @staticmethod
    async def update_user(db: AsyncSession, user, update_data: dict):
        for key, value in update_data.items():
            setattr(user, key, value)
        return await UserRepository.update(db, user)

    @staticmethod
    async def delete_user(db: AsyncSession, user):
        await UserRepository.delete(db, user)
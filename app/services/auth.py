from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.users import User
from app.schemas.users import UserCreate, UserLogin
from app.repositories.user_repo import UserRepository
from app.core.security import hash_password, verify_password, create_access_token



class AuthService:

    @staticmethod
    async def register(db: AsyncSession, user_data: UserCreate):
        existing_user = await UserRepository.get_by_email(db, user_data.email)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

        user = User(
            name=user_data.name,
            email=user_data.email,
            hashed_password=hash_password(user_data.password),
            role=user_data.role
        )

        return await UserRepository.create(db, user)

    @staticmethod
    async def login(db: AsyncSession, credentials: UserLogin):
        user = await UserRepository.get_by_email(db, credentials.email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is inactive"
            )

        if not verify_password(
            credentials.password,
            user.hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        token = create_access_token(
            {
                "sub": str(user.id),
                "role": user.role
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }
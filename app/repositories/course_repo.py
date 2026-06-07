from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.courses import Course


class CourseRepository:

    @staticmethod
    async def create(db: AsyncSession, course: Course):
        db.add(course)
        await db.commit()
        await db.refresh(course)
        return course

    @staticmethod
    async def get_by_id(db: AsyncSession, course_id: int):
        result = await db.execute(select(Course).where(Course.id == course_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_code(db: AsyncSession, code: str):
        result = await db.execute(select(Course).where(Course.code == code))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(db: AsyncSession):
        result = await db.execute(select(Course))
        return result.scalars().all()

    @staticmethod
    async def get_active_courses(db: AsyncSession):
        result = await db.execute(select(Course).where(Course.is_active == True))
        return result.scalars().all()

    @staticmethod
    async def update(db: AsyncSession, course: Course):
        await db.commit()
        await db.refresh(course)
        return course

    @staticmethod
    async def delete(db: AsyncSession, course: Course):
        await db.delete(course)
        await db.commit()
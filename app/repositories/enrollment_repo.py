from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.enrollments import Enrollment


class EnrollmentRepository:

    @staticmethod
    async def create(db: AsyncSession, enrollment: Enrollment):
        db.add(enrollment)
        await db.commit()
        await db.refresh(enrollment)
        return enrollment

    @staticmethod
    async def get_by_id(db: AsyncSession, enrollment_id: int):
        result = await db.execute(select(Enrollment).where(Enrollment.id == enrollment_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(db: AsyncSession):
        result = await db.execute(select(Enrollment))
        return result.scalars().all()

    @staticmethod
    async def get_user_course(db: AsyncSession, user_id: int, course_id: int):
        result = await db.execute(select(Enrollment).where(Enrollment.user_id == user_id, Enrollment.course_id == course_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_course_enrollments(db: AsyncSession, course_id: int):
        result = await db.execute(select(Enrollment).where(Enrollment.course_id == course_id))
        return result.scalars().all()

    @staticmethod
    async def count_course_enrollments(db: AsyncSession, course_id: int):
        result = await db.execute(select(Enrollment).where(Enrollment.course_id == course_id))
        return len(result.scalars().all())

    @staticmethod
    async def delete(db: AsyncSession, enrollment: Enrollment):
        await db.delete(enrollment)
        await db.commit()
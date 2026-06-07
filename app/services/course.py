from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.courses import Course
from app.schemas.courses import CourseCreate, CourseUpdate
from app.repositories.course_repo import CourseRepository


class CourseService:

    @staticmethod
    async def create_course(db: AsyncSession, course_data: CourseCreate):

        existing_course = (
            await CourseRepository.get_by_code(db, course_data.code)
        )
        if existing_course:
            raise HTTPException(
                status_code=400,
                detail="Course code already exists"
            )

        course = Course(title=course_data.title, code=course_data.code, capacity=course_data.capacity)

        return await CourseRepository.create(db, course)

    @staticmethod
    async def get_all_courses(db: AsyncSession):
        return await CourseRepository.get_active_courses(db)

    @staticmethod
    async def get_course_by_id(db: AsyncSession, course_id: int):

        course = await CourseRepository.get_by_id(db, course_id)
        if not course:
            raise HTTPException(
                status_code=404,
                detail="Course not found"
            )

        return course

    @staticmethod
    async def update_course(db: AsyncSession, course, course_data: CourseUpdate):

        updates = (
            course_data.model_dump(
                exclude_unset=True
            )
        )

        for key, value in updates.items():
            setattr(course, key, value)

        return await CourseRepository.update(db, course)

    @staticmethod
    async def delete_course(db: AsyncSession, course):

        await CourseRepository.delete(db, course)
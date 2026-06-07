from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.enrollments import Enrollment
from app.repositories.course_repo import CourseRepository
from app.repositories.enrollment_repo import EnrollmentRepository



class EnrollmentService:

    @staticmethod
    async def enroll_student(db: AsyncSession, user, course_id: int):
        course = await CourseRepository.get_by_id(db, course_id)
        if not course:
            raise HTTPException(
                status_code=404,
                detail="Course not found"
            )

        if not course.is_active:
            raise HTTPException(
                status_code=400,
                detail="Course inactive"
            )

        existing = (
            await EnrollmentRepository.get_user_course(db, user.id, course_id)
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Already enrolled"
            )

        count = (
            await EnrollmentRepository.count_course_enrollments(db, course_id)
        )

        if count >= course.capacity:
            raise HTTPException(
                status_code=400,
                detail="Course is full"
            )

        enrollment = Enrollment(
            user_id=user.id,
            course_id=course_id
        )

        return await EnrollmentRepository.create(db, enrollment)

    @staticmethod
    async def deregister_student(db: AsyncSession, user, course_id: int):

        enrollment = (
            await EnrollmentRepository.get_user_course(db, user.id, course_id)
        )

        if not enrollment:
            raise HTTPException(
                status_code=404,
                detail="Enrollment not found"
            )

        await EnrollmentRepository.delete(db, enrollment)

    @staticmethod
    async def get_all_enrollments(db: AsyncSession):

        return await EnrollmentRepository.get_all(db)

    @staticmethod
    async def get_course_enrollments(db: AsyncSession, course_id: int):

        return await EnrollmentRepository.get_course_enrollments(db, course_id)
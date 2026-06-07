from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.deps import get_async_db, get_current_student, get_current_admin
from app.schemas.enrollments import EnrollmentCreate, EnrollmentRead
from app.services.enrollment import EnrollmentService


router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.post("/", response_model=EnrollmentRead, status_code=201)
async def enroll(enrollment_data: EnrollmentCreate, db: AsyncSession = Depends(get_async_db), current_user=Depends(get_current_student)):
    return await EnrollmentService.enroll_student(db, current_user, enrollment_data.course_id)

@router.delete("/{course_id}")
async def deregister(course_id: int, db: AsyncSession = Depends(get_async_db), current_user=Depends(get_current_student)):
    await EnrollmentService.deregister_student(db, current_user, course_id)

    return {"message": "Successfully deregistered"}

@router.get("/", response_model=list[EnrollmentRead])
async def get_all_enrollments(db: AsyncSession = Depends(get_async_db), admin=Depends(get_current_admin)):

    return await EnrollmentService.get_all_enrollments(db)

@router.get("/course/{course_id}", response_model=list[EnrollmentRead])
async def get_course_enrollments(course_id: int, db: AsyncSession = Depends(get_async_db), admin=Depends(get_current_admin)):

    return await EnrollmentService.get_course_enrollments(db, course_id)
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.deps import get_async_db, get_current_admin
from app.schemas.courses import CourseCreate, CourseRead, CourseUpdate
from app.services.course import CourseService

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/", response_model=list[CourseRead])
async def get_courses(db: AsyncSession = Depends(get_async_db)):
    return await CourseService.get_all_courses(db)

@router.get("/{course_id}", response_model=CourseRead)
async def get_course(course_id: int, db: AsyncSession = Depends(get_async_db)):
    return await CourseService.get_course_by_id(db, course_id)

@router.post("/", response_model=CourseRead, status_code=status.HTTP_201_CREATED)
async def create_course(course_data: CourseCreate, db: AsyncSession = Depends(get_async_db), admin=Depends(get_current_admin)):
    return await CourseService.create_course(db, course_data)

@router.patch("/{course_id}", response_model=CourseRead)
async def update_course(course_id: int, course_data: CourseUpdate, db: AsyncSession = Depends(get_async_db), admin=Depends(get_current_admin)):
    course = await CourseService.get_course_by_id(db, course_id)
    return await CourseService.update_course(db, course, course_data)

@router.delete("/{course_id}")
async def delete_course(course_id: int, db: AsyncSession = Depends(get_async_db), admin=Depends(get_current_admin)):
    course = await CourseService.get_course_by_id(db, course_id)
    await CourseService.delete_course(db, course)
    
    return {"message": "Course deleted successfully"}

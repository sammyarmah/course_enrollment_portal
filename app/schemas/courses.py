from pydantic import BaseModel, Field
from typing import Optional


class CourseBase(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    code: str = Field(min_length=2, max_length=20)
    capacity: int = Field(gt=0)


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    title: Optional[str]= None
    code: Optional[str]= None
    capacity: Optional[int]= Field(default=None, gt=0)
    is_active: Optional[bool] = None


class CourseRead(CourseBase):
    id: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }
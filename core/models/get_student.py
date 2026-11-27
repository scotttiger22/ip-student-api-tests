from pydantic import BaseModel
from typing import List, Optional


class Student(BaseModel):
    id: int
    name: str
    email: str
    gender: str
    phone_no: Optional[str] = None
    status: int


class StudentsResponse(BaseModel):
    status: int
    students: List[Student]


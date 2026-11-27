from pydantic import BaseModel
from typing import Literal, Optional


class Student(BaseModel):
    id: int
    name: str
    email: str
    gender: Literal["male", "female"]
    phone_no: Optional[str] = None
    status: Literal[0, 1]


class StudentUpdatedResponse(BaseModel):
    message: str
    status: int
    student: Student


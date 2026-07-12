from pydantic import BaseModel

class StudentGrades(BaseModel):

    student_id: int
    grade: float
    subject: str

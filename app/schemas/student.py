from pydantic import BaseModel

class Student(BaseModel):
    name: str
    last_name: str
    status: bool
from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str  # Nome do aluno
    last_name: str  # Sobrenome do aluno
    status: bool  # Indica se o aluno está ativo/matriculado
    subject: str  # Nome da disciplina
    grade: float  # Nota obtida pelo aluno na disciplina
    absences: int  # Quantidade de faltas do aluno na disciplina

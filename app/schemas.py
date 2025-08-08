from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    name: str
    email: EmailStr
    age: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    name: str | None = None
    email: EmailStr | None = None
    age: int | None = None

class StudentOut(StudentBase):
    id: int

    class Config:
        orm_mode = True
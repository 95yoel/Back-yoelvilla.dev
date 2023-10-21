from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    surname: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str


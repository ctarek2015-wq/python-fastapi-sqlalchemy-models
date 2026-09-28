from pydantic import BaseModel


class UserFormSchema(BaseModel):
    username: str
    email: str
    password: str


class UserSchema(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True

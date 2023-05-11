from pydantic import BaseModel


class TokenCreate(BaseModel):
    email: str
    password: str


class TokenData(BaseModel):
    access_token: str
    user_id: str
    email: str

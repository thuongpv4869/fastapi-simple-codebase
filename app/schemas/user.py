from pydantic import BaseModel


class UserMe(BaseModel):
    id: int
    full_name: str = ""
    email: str
    phone: str = ""

    class Config:
        orm_mode = True


class UserAvatar(BaseModel):
    avatar_url: str

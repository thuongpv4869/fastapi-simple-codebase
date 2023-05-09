from datetime import date
from typing import Optional

from pydantic import BaseModel


class CustomerCreate(BaseModel):
    full_name: Optional[str] = ""
    email: str
    phone: Optional[str] = ""
    address: Optional[str] = ""


class CustomerUpdate(BaseModel):
    full_name: Optional[str]
    phone: Optional[str]
    address: Optional[str]


class Customer(BaseModel):
    id: int
    full_name: str = ""
    email: str
    phone: str = ""
    address: str = ""

    class Config:
        orm_mode = True


class CustomerIdentityCard(BaseModel):
    id: int
    card_number: str
    full_name: str
    date_of_birth: date
    gender: str
    nationality: str
    place_of_origin: str
    place_of_residence: str
    date_of_expiry: date
    date_of_issue: date

    class Config:
        orm_mode = True

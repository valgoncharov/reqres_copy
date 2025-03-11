from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    avatar: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar: Optional[str] = None
    password: Optional[str] = None


class UserInDB(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None


class Support(BaseModel):
    url: str
    text: str


class UserResponse(BaseModel):
    data: UserInDB
    support: Support


class UserListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserInDB]
    support: Support

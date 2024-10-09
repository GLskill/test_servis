from pydantic import BaseModel, EmailStr
from typing import Optional


class Employee(BaseModel):
    fullName: str
    email: EmailStr
    phone: str
    isProbationPeriodPassed: bool = False
    isPermanentEmployee: bool = False


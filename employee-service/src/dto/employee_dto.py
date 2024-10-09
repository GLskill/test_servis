from pydantic import BaseModel, EmailStr


class EmployeeDTO(BaseModel):
    fullName: str
    email: EmailStr
    phone: str
    isProbationPeriodPassed: bool = False
    isPermanentEmployee: bool = False


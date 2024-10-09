from typing import List

from fastapi import APIRouter
from src.dto.employee_dto import EmployeeDTO
from src.services.employee_service import EmployeeService

router = APIRouter()
service = EmployeeService()


@router.post("/employees", response_model=EmployeeDTO)
def add_employee(employee: EmployeeDTO):
    return service.add_employee(employee)


@router.get("/employees", response_model=List[EmployeeDTO])
def get_all_employees():
    return service.get_all_employees()


@router.get("/employees/on_probation", response_model=List[EmployeeDTO])
def get_employees_on_probation():
    return service.get_employees_on_probation()


@router.put("/employees/{id}", response_model=EmployeeDTO)
def update_employee(id: str, employee: EmployeeDTO):
    return service.update_employee(id, employee)


@router.delete("/employees/{id}")
def delete_employee(id: str):
    service.delete_employee(id)
    return {"message": "Employee deleted"}


@router.patch("/employees/{id}/end_probation", response_model=EmployeeDTO)
def end_probation(id: str):
    return service.end_probation(id)

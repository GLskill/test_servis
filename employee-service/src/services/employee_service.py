from typing import List
from src.dao.employee_dao import EmployeeDAO
from src.dto.employee_dto import EmployeeDTO


class EmployeeService:
    def __init__(self):
        self.dao = EmployeeDAO()

    def add_employee(self, employee: EmployeeDTO):
        return self.dao.create_employee(employee)

    def get_all_employees(self) -> List[EmployeeDTO]:
        return self.dao.read_all_employees()

    def get_employees_on_probation(self) -> List[EmployeeDTO]:
        return self.dao.read_employees_on_probation()

    def update_employee(self, id: str, employee: EmployeeDTO):
        return self.dao.update_employee(id, employee)

    def delete_employee(self, id: str):
        self.dao.delete_employee(id)

    def end_probation(self, id: str):
        employee = self.dao.read_employee_by_id(id)
        employee.isProbationPeriodPassed = True
        return self.dao.update_employee(id, employee)

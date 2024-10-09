from bson import ObjectId
from src.models.employee import Employee
from src.utils.database import db


class EmployeeDAO:
    def create_employee(self, employee: Employee):
        employee_dict = employee.dict()
        db.employees.insert_one(employee_dict)
        return employee

    def read_all_employees(self):
        employees = db.employees.find()
        return [Employee(**employee) for employee in employees]

    def read_employees_on_probation(self):
        employees = db.employees.find({"isProbationPeriodPassed": False})
        return [Employee(**employee) for employee in employees]

    def update_employee(self, id: str, employee: Employee):
        db.employees.update_one({"_id": ObjectId(id)}, {"$set": employee.dict()})
        return employee

    def delete_employee(self, id: str):
        db.employees.delete_one({"_id": ObjectId(id)})

    def read_employee_by_id(self, id: str):
        employee = db.employees.find_one({"_id": ObjectId(id)})
        return Employee(**employee) if employee else None

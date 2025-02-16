from abc import ABC
from Employee import Employee


class FullTimeEmployee(Employee, ABC):
    def __init__(self, _name, _employee_id, _salary):
        Employee.__init__(self, _name, _employee_id)
        self._salary = _salary

    def get_salary(self):
        return self._salary

    def calculate_pay(self):
        return f"Full time employee pay: {self._salary}"

employee = FullTimeEmployee(
    "Future",
    "00011",
    500000
)
print("Employee Name:", employee.get_name())
print("Employee ID:", employee.get_employee_id())
print("Employee salary",employee.get_salary())
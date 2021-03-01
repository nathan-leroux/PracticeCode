#employee
from hr import(
    Salary_Employee,
    Comission_Employee,
    Hourly_Employee
)
from productivity import(
    Manager_Role,
    Secretary_Role,
    Factory_Role,
    Sales_Role
)
    
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Manager(Employee, Manager_Role, Salary_Employee):
    def __init__(self, id, name, salary):
        Salary_Employee.__init__(self, salary)
        super().__init__(id, name)

class Secretary(Employee, Secretary_Role, Salary_Employee):
    def __init__(self, id, name, salary):
        Salary_Employee.__init__(self, salary)
        super().__init__(id, name)

class Factory(Employee, Factory_Role, Hourly_Employee):
    def __init__(self, id, name, hours, rate):
        Hourly_Employee.__init__(self, hours, rate)
        super().__init__(id, name)

class Sales(Employee, Sales_Role, Comission_Employee):
    def __init__(self, id, name, salary, comission):
        Comission_Employee.__init__(self, salary, comission)
        super().__init__(id, name)

class TempSecretary(Employee, Secretary_Role, Hourly_Employee):
    def __init__(self, id, name, hours, rate):
        Hourly_Employee.__init__(self, hours, rate)
        super().__init__(id, name)

#employee
from hr import EmployeePayroll
from productivity import Productivity
from address import AddressBook

class CreateEmployee:
    def __init__(self):
        self._employee = [
            {
                'id' : 1,
                'name' : 'Bob'
            },
            {
                'id' : 2,
                'name' : 'Clive'
            },
            {
                'id' : 3,
                'name' : 'Jeff'
            },
            {
                'id' : 4,
                'name' : 'Gustavo'
            },
            {
                'id' : 5,
                'name' : 'Beckiny'
            }
        ]
        self.address = AddressBook()
        self.payroll = EmployeePayroll()
        self.productivity = Productivity()

    def Employees(self):
        return [self._create_employees(**data) for data in self._employee]

    def _create_employees(self, id, name):
        employee_address = self.address.Get_Address(id)
        employee_role = self.productivity.GetRole(id)
        employee_pay = self.payroll.GetPayment(id)
        return Employee(id, name, employee_address, employee_role, employee_pay)
    
class Employee:
    def __init__(self, id, name, address, role, payment):
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payment = payment

    def work(self, hours):
        duties = self.role.work(hours)
        print(f'{self.id} : {self.name}')
        print(f'{duties}',end='\n\n')
        self.payment.hours_worked(hours)

    def calc_payroll(self):
        return self.payment.calc_payroll()


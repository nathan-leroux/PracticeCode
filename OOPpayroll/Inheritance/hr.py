# OOP payroll
# following the real python tute

class EmployeePayroll:
    def PrintPayroll(self, employees):
        print('Employee Payroll')
        print('================')
        print('')
        for employee in employees:
            print(f'{employee.id} - {employee.name} paycheck: {employee.calc_payroll()}',end='\n\n')

class Salary_Employee:
    def __init__(self, salary):
        self.salary = salary

    def calc_payroll(self):
        return self.salary

class Comission_Employee(Salary_Employee):
    def __init__(self, salary, comission):
        super().__init__(salary)
        self.comission = comission

    def calc_payroll(self):
        fixed = super().calc_payroll()
        return fixed + self.comission

class Hourly_Employee:
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calc_payroll(self):
        return self.hours * self.rate


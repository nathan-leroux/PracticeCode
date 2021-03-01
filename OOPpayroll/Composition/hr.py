# OOP payroll
# following the real python tute

class EmployeePayroll:
    def __init__(self):
        self._payment = {
            1 : Salary_Employee(1500),
            2 : Salary_Employee(1000),
            3 : Comission_Employee(800, 200),
            4 : Hourly_Employee(40),
            5 : Hourly_Employee(15)
            }

    def GetPayment(self, id):
        data = self._payment.get(id)
        if data == None:
            raise ValueError('oh shit dawg, payroll broke')
        return data
    
    def PrintPayroll(self, employees):
        print('Employee Payroll')
        print('================')
        print('')
        for employee in employees:
            print(f'{employee.id} - {employee.name} paycheck: {employee.calc_payroll()}',end='\n\n')

class PayrollPolicy:
    def __init__(self):
        self.tracked_hours = 0

    def hours_worked(self, hours):
        self.tracked_hours += hours

class Salary_Employee(PayrollPolicy):
    def __init__(self, salary):
        super().__init__()
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

class Hourly_Employee(PayrollPolicy):
    def __init__(self, rate):
        super().__init__()
        self.rate = rate

    def calc_payroll(self):
        return self.tracked_hours * self.rate


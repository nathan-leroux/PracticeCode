#program
from hr import EmployeePayroll
from productivity import Productivity
from employee import CreateEmployee

emp = CreateEmployee()
epay = EmployeePayroll()
prd = Productivity()
employees = emp.Employees()
prd.WorkerProductivity(employees, 40)
epay.PrintPayroll(employees)

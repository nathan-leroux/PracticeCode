#program
import hr
import employee
import productivity

Elist = [employee.Manager(1, 'Bob', 1000),
        employee.Secretary(2, 'Clive', 900),
        employee.Factory(3, 'Jeff', 20, 5),
        employee.Sales(4, 'Gustavo', 900, 200),
        employee.TempSecretary(5, 'Beckiny', 10, 10)]

ps = productivity.Productivity()
ps.WorkerProductivity(Elist, 40)

payroll = hr.EmployeePayroll()
payroll.PrintPayroll(Elist)


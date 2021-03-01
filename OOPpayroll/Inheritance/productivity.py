#productivity

class Productivity:
    def WorkerProductivity(self, employees, hours):
        print('Worker Productivity')
        print('===================')
        print('')
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name}: {result}')
            
class Manager_Role:
    def work(self, hours):
        return f'screams and shouts for {hours} hours.'

class Secretary_Role:
    def work(self, hours):
        return f'does paperwork for {hours} hours.'

class Factory_Role:
    def work(self, hours):
        return f'slaves away for {hours} hours.'

class Sales_Role:
    def work(self, hours):
        return f'sits on the phone for {hours} hours.'
    

#productivity

class Productivity:
    def __init__(self):
        self._roles = {
            1 : Manager_Role,
            2 : Secretary_Role,
            3 : Sales_Role,
            4 : Factory_Role,
            5 : Secretary_Role
            }
    def GetRole(self, id):
        data = self._roles.get(id)
        if data == None:
            raise ValueError('oh shit dawg, roles broke')
        return data()
    
    def WorkerProductivity(self, employees, hours):
        print('Worker Productivity')
        print('===================')
        print('')
        for employee in employees:
            employee.work(hours)
            
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
    

class AddressBook:
    def __init__(self):
        self._employee_address = {
            1: Address('15', 'Dundee Court', 'Duncraig', 'WA', '6023'),
            2: Address('49', 'Ayton Way', 'Duncraig', 'WA', '6023'),
            3: Address('23', 'Ideas Avenue', 'South Park', 'QLD', '4926'),
            4: Address('88', 'Sleep Drive', 'Padbury', 'ACT', '1111'),
            5: Address('202', 'Ocun Cresent', 'Craigie', 'SA', '4598')
            }

    def Get_Address(self, id):
        data = self._employee_address.get(id)
        if data == None:
            raise ValueError('oh shit dawg, it broke')
        return data

class Address:
    def __init__(self, no, street, suburb, state, postcode):
        self.no = no
        self.street = street
        self.suburb = suburb
        self.state = state
        self.postcode = postcode
    def __str__(self):
        string = f'{self.no} {self.street},\n{self.suburb}, {self.state}, {self.postcode}'
        return string


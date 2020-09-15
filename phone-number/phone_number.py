class PhoneNumber:
    def __init__(self, number: str):
        self.number = ''.join(list(filter(str.isdigit, number)))
        self.validate()

    def validate(self):
        if len(self.number) == 11 and self.number[0] == '1':
            self.number = self.number[1:]
        if len(self.number) != 10:
            raise ValueError('Phone number is invalid')
        if self.number[0] == '1' or self.number[0] == '0':
            raise ValueError('Invalid Area Code')
        if self.number[3] == '1' or self.number[3] == '0':
            raise ValueError('Invalid Exchange Code')

    @property
    def area_code(self):
        return self.number[0:3]

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"

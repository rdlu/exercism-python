import re


class PhoneNumber:
    def __init__(self, number: str):
        self.number = self.__clean_number(number)
        self.__validate()

    def __clean_number(self, digits: str) -> str:
        num = re.sub(r'[^\w]', r'', digits)
        if len(num) == 11 and num[0] == '1':
            num = num[1:]
        return num

    def __validate(self):
        if len(self.number) != 10:
            raise ValueError('Phone number is invalid')
        if self.number[0] == '1' or self.number[0] == '0':
            raise ValueError('Invalid Area Code')
        if self.number[3] == '1' or self.number[3] == '0':
            raise ValueError('Invalid Exchange Code')

    @property
    def area_code(self):
        return self.number[0:3]

    @property
    def exchange_code(self):
        return self.number[3:6]

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.number[6:]}"

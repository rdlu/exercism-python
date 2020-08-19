class Luhn:
    def __init__(self, card_num: str):
        self._reversed_card_num = card_num.replace(' ', '')[::-1]
        self._even_digits = self._reversed_card_num[1::2]
        self._odd_digits = self._reversed_card_num[::2]

    def valid(self) -> bool:
        if str.isnumeric(self._reversed_card_num) and len(self._reversed_card_num) > 1:
            return self._sum_card() % 10 == 0
        else: 
            return False
        
    def _sum_card(self) -> int:
        even_digits_sum = 0
        for digit in self._even_digits:
            x = int(digit) * 2
            even_digits_sum += x if x <= 9 else x - 9
        return even_digits_sum + sum([int(x) for x in self._odd_digits])

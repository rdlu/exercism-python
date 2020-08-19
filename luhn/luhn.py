class Luhn:
    def __init__(self, card_num: str):
        self._reversed_card_num = card_num.replace(' ', '')[::-1]
        self._even_digits = self._reversed_card_num[1::2]
        self._odd_digits = self._reversed_card_num[::2]

    def valid(self) -> bool:
        if not str.isnumeric(self._reversed_card_num) or len(self._reversed_card_num) < 2:
            return False
        return self._sum_card() % 10 == 0
        
    def _sum_card(self) -> int:
        card_sum = 0
        for digit in self._even_digits:
            current_digit = int(digit) * 2
            if current_digit > 9:
                current_digit -= 9
            card_sum += current_digit
        return card_sum + sum([int(x) for x in self._odd_digits])

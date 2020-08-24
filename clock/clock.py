class Clock:
    def __init__(self, hour, minutes):
        self._hour, self._minutes = self.convert_to_clock(hour, minutes)

    def __repr__(self) -> str:
        return "{}:{}".format(str(self._hour).zfill(2), str(self._minutes).zfill(2))

    def __eq__(self, other: 'Clock') -> bool:
        return str(self) == str(other)

    def __add__(self, minutes: int) -> 'Clock':
        self._hour, self._minutes = self.convert_to_clock(0, self.convert_to_minutes() + minutes)
        return self

    def __sub__(self, minutes: int) -> 'Clock':
        self._hour, self._minutes = self.convert_to_clock(0, self.convert_to_minutes() - minutes)
        return self

    def convert_to_minutes(self) -> int:
        return self._hour * 60 + self._minutes

    def convert_to_clock(self, hours: int, minutes: int) -> (int, int):
        hour = ((hours % 24) + ((minutes // 60) % 24)) % 24
        minute = minutes % 60
        return (hour, minute)
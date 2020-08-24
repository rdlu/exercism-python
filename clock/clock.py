class Clock:
    def __init__(self, hour: int, minutes: int):
        self._minutes = (minutes + 60 * hour) % (60*24)

    def __repr__(self) -> str:
        return "{:02d}:{:02d}".format(*divmod(self._minutes, 60))

    def __eq__(self, other: 'Clock') -> bool:
        return repr(self) == repr(other)

    def __add__(self, minutes: int) -> 'Clock':
        return Clock(0, (self._minutes + minutes) % (60*24))

    def __sub__(self, minutes: int) -> 'Clock':
        return Clock(0, (self._minutes - minutes) % (60*24))
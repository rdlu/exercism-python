class Clock:
    def __init__(self, hour, minutes):
        self._minutes = (minutes + 60 * hour) % (60*24)

    def __repr__(self) -> str:
        return "{}:{}".format(str(self._minutes // 60).zfill(2), str(self._minutes % 60).zfill(2))

    def __eq__(self, other: 'Clock') -> bool:
        return repr(self) == repr(other)

    def __add__(self, minutes: int) -> 'Clock':
        self._minutes = (self._minutes + minutes) % (60*24)
        return self

    def __sub__(self, minutes: int) -> 'Clock':
        self._minutes = (self._minutes - minutes) % (60*24)
        return self
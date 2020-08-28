class SpaceAge:
    orbital_periods = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132,
    }
    earth_year = 31557600

    def __init__(self, seconds: int):
        self.seconds = seconds

    def calculate(self, planet: str) -> float:
        return round(self.seconds / self.earth_year / self.orbital_periods[planet], 2)

    def __getattr__(self, name: str):
        if not name[3:] in self.orbital_periods.keys():
            raise AttributeError("'tuple' object has no attribute '%s'" % name)

        def method(*args):
            return self.calculate(name[3:])
        return method


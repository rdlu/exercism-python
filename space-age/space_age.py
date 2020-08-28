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
        for planet in self.orbital_periods.keys():
            setattr(self, "on_"+planet, self.calculate(planet))

    def calculate(self, planet: str) -> float:
        return lambda: round(self.seconds / self.earth_year / self.orbital_periods[planet], 2)


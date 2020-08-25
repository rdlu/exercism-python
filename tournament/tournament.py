class Team():
    def __init__(self, name: str):
        self.name = name
        self.won = 0
        self.tied = 0
        self.lost = 0

    def total_points(self) -> int:
        return self.won * 3 + self.tied * 1 + self.lost * 0

    def matches_played(self) -> int:
        return self.won + self.lost + self.tied

    def results(self) -> str:
        return Team.line_format(self.name, self.matches_played(), self.won, self.tied, self.lost, self.total_points())

    @staticmethod
    def header() -> str:
        return Team.line_format('Team', 'MP', ' W', ' D', ' L', ' P')

    @staticmethod
    def line_format(name: str, mp, w, d, l, p) -> str:
        return f'{name:30} | {mp:2} | {w:2} | {d:2} | {l:2} | {p:2}'


def tally(rows: list(str)) -> list(str):
    totals = {}
    for line in rows:
        (home, away, result) = line.split(';')
        totals.setdefault(home, Team(home))
        totals.setdefault(away, Team(away))
        if result == 'win':
            totals[home].won += 1
            totals[away].lost += 1
        elif result == 'loss':
            totals[home].lost += 1
            totals[away].won += 1
        elif result == 'draw':
            totals[home].tied += 1
            totals[away].tied += 1

    table = []
    table.append(Team.header())
    for team in sorted(totals.values(), key=lambda team: (-team.won, -team.total_points(), team.name)):
        table.append(team.results())

    return table
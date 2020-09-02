from datetime import date
from calendar import monthcalendar

get_day_index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
slang_index = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, "last": -1}

class MeetupDayException(Exception):
    def __init__(self, message):
        print(message)

def meetup(year: int, month: int, week: str, day_of_week: str) -> 'date':
    month_days_per_week = monthcalendar(year, month)
    day_index = get_day_index.index(day_of_week)
    days = [week_days[day_index] for week_days in month_days_per_week if week_days[day_index] > 0]

    if week == 'teenth':
        for d in days:
            if d in range(13, 20):
                return date(year, month, d)
    else:
        try:
            return date(year, month, days[slang_index[week]])
        except IndexError:
            raise MeetupDayException('The selected day doesn\'t exists')
        
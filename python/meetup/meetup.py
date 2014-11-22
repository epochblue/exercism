import datetime


WHICH_TO_INDEX = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, 'last': -1}


def meetup_day(year, month, dow, which):
    by_dow = { 'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [],
               'Friday': [], 'Saturday': [], 'Sunday': []}

    # Group the days of the month by their days of the week
    dt = datetime.date(year, month, 1) 
    while dt.month == month:
        day_name = dt.strftime('%A')
        by_dow[day_name].append(dt.day)
        dt = dt + datetime.timedelta(days=1)

    # ...then get the right day
    if which in WHICH_TO_INDEX:
        index = WHICH_TO_INDEX[which]
        day = by_dow[dow][index]

    if which == 'teenth':
        day = [d for d in by_dow[dow] if 12 < d < 20][0]

    return datetime.date(year, month, day)


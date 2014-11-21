def is_leap_year(year):
    """Determine if the given year is a valid leap year."""
    return (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0)

from datetime import timedelta

def add_gigasecond(dt):
    """Calculate the date that someone will celebrate their 1Gsanniversary."""
    return dt + timedelta(seconds=10**9)


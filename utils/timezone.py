from datetime import datetime
from zoneinfo import ZoneInfo


NAIROBI_TZ = ZoneInfo("Africa/Nairobi")


def nairobi_now():
    """
    Returns the current datetime in Africa/Nairobi.
    """
    return datetime.now(NAIROBI_TZ)


def nairobi_today():
    """
    Returns today's date in Africa/Nairobi.
    """
    return datetime.now(NAIROBI_TZ).date()
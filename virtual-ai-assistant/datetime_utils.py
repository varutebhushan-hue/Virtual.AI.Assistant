from datetime import datetime


def get_current_time():
    now = datetime.now()
    formatted = now.strftime("%I:%M %p").lstrip("0")
    return f"It's currently {formatted}."


def get_current_date():
    """
    Return today's date as a friendly formatted string.
    Example: "Sunday, September 06, 2026"
    """
    now = datetime.now()
    formatted = now.strftime("%A, %B %d, %Y")
    return f"Today's date is {formatted}."


def get_current_hour():
    """
    Return just the current hour (0-23) as an integer.

    Used by ai_concepts.recommend_activity() to demonstrate a
    rule-based / classification-style decision (FR-13).
    """
    return datetime.now().hour

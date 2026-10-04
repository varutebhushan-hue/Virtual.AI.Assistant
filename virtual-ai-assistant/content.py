"""
content.py
----------
Stores predefined lists of quotes, jokes, and facts, and provides
random-selection functions (FR-06, FR-07, FR-08).

AI/Python concept demonstrated:
- Lists as a simple data store.
- The 'random' module for selection.
- Conceptually, this mirrors (at a beginner level) how a recommendation
  engine picks one item from a candidate pool — see PRD section 20.
"""

import random

QUOTES = [
    "The best way to predict the future is to create it.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "Small steps every day lead to big results.",
    "Your only limit is your mind.",
    "Discipline is the bridge between goals and accomplishment.",
    "Progress, not perfection.",
]

JOKES = [
    "Why did the developer go broke? Because they used up all their cache.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Why was the JavaScript developer sad? Because they didn't know how to 'null' their feelings.",
    "Why did the computer go to therapy? It had too many unresolved issues.",
]

FACTS = [
    "The first computer virus was created in 1983 and was called the Elk Cloner.",
    "Python was named after the comedy group Monty Python, not the snake.",
    "The first 'bug' in computing was an actual moth found in a relay in 1947.",
    "More than 90% of the world's currency exists only digitally.",
    "The QWERTY keyboard layout was originally designed to slow typists down.",
]


def get_random_quote():
    """Return a random motivational quote (FR-06)."""
    return random.choice(QUOTES)


def get_random_joke():
    """Return a random joke (FR-07)."""
    return random.choice(JOKES)


def get_random_fact():
    """Return a random fact (FR-08)."""
    return random.choice(FACTS)

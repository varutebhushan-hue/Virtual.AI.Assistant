COMMANDS = [
    ("time", "show current time"),
    ("date", "show current date"),
    ("calculate <num> <op> <num>", "do a calculation (e.g., calculate 12 + 8)"),
    ("joke", "tell a joke"),
    ("quote", "motivational quote"),
    ("fact", "random fact"),
    ("game", "play the number guessing game"),
    ("recommend", "get an activity recommendation based on the time of day"),
    ("perceptron", "run a simplified neural-network neuron demo"),
    ("help", "show this list again"),
    ("exit / quit / bye", "quit the assistant"),
]


def print_help():
    lines = ["Assistant:"]
    for command, description in COMMANDS:
        lines.append(f"  - {command:<28} {description}")
    return "\n".join(lines)

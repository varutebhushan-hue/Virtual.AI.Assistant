def get_user_name():
    """
    Ask the user for their name and return it as a clean string.

    Demonstrates: input handling, string methods (.strip(), .title()).
    """
    print("Assistant: Hi! I'm Mini Alexa. What's your name?")
    name = input("You: ").strip()

    # Fallback if the user just presses Enter with no input.
    if not name:
        name = "Friend"

    return name.title()


def build_greeting(name):
    return (
        f"Assistant: Nice to meet you, {name}! Type 'help' "
        f"to see what I can do.\n"
    )


def build_farewell(name):
    return f"Assistant: Goodbye, {name}! Have a great day."

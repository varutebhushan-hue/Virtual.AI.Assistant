OPERATOR_ALIASES = {
    "+": "+", "plus": "+", "add": "+",
    "-": "-", "minus": "-", "subtract": "-",
    "*": "*", "x": "*", "times": "*", "multiply": "*",
    "/": "/", "divide": "/", "divided": "/",
}


def parse_expression(text):
    """
    Extract (num1, operator, num2) from a command like:
      "calculate 12 + 8"
      "calculate 5 divide 0"

    Returns a tuple (num1, operator, num2) on success, or None if the
    command could not be parsed.

    Demonstrates: list/string operations, iteration, basic parsing logic.
    """
    tokens = text.lower().replace("calculate", "").split()

    numbers = []
    operator = None

    for token in tokens:
        if token in OPERATOR_ALIASES:
            operator = OPERATOR_ALIASES[token]
            continue
        try:
            numbers.append(float(token))
        except ValueError:
            continue

    if operator is None or len(numbers) < 2:
        return None

    return numbers[0], operator, numbers[1]


def calculate(num1, operator, num2):
    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2  # may raise ZeroDivisionError
        else:
            return "I don't recognize that operator. Try +, -, *, or /."

        if result == int(result):
            result = int(result)

        return f"The result is {result}"

    except ZeroDivisionError:
        return "I can't divide by zero — try a different number."
    except Exception:
        return "Something went wrong with that calculation — please try again."


def respond_calculator(user_text):
    parsed = parse_expression(user_text)

    if parsed is None:
        return (
            "I couldn't understand that calculation. "
            "Try something like: calculate 12 + 8"
        )

    num1, operator, num2 = parsed
    return calculate(num1, operator, num2)

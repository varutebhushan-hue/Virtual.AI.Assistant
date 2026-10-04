import greetings
import datetime_utils
import calculator
import content
import game
import ai_concepts
import help_menu


EXIT_KEYWORDS = ("exit", "quit", "bye")


def normalize(text):
    """Lowercase and strip whitespace from user input before matching."""
    return text.strip().lower()


def route_command(user_text, name):
    normalized = normalize(user_text)

    if any(word in normalized for word in EXIT_KEYWORDS):
        return None  # Signals the main loop to end the session.

    if "help" in normalized:
        return help_menu.print_help()

    if "time" in normalized:
        return datetime_utils.get_current_time()

    if "date" in normalized:
        return datetime_utils.get_current_date()

    if "calculate" in normalized or "calc" in normalized:
        return calculator.respond_calculator(normalized)

    if "quote" in normalized:
        return content.get_random_quote()

    if "joke" in normalized:
        return content.get_random_joke()

    if "fact" in normalized:
        return content.get_random_fact()

    if "game" in normalized or "guess" in normalized:
        game.play_guessing_game()
        return None

    if "recommend" in normalized or "activity" in normalized:
        return ai_concepts.recommend_activity()

    if "perceptron" in normalized or "neuron" in normalized:
        return ai_concepts.perceptron_demo()

    if "hi" in normalized or "hello" in normalized:
        return f"Assistant: Hi again, {name}! Type 'help' if you need a reminder of what I can do."

    return "Assistant: I'm not sure I understood that — type 'help' to see what I can do."


def main():
    name = greetings.get_user_name()
    print(greetings.build_greeting(name))

    while True:
        try:
            user_text = input("You: ")

            if not user_text.strip():
                print("Assistant: I didn't catch that — try typing a command, or 'help'.")
                continue

            response = route_command(user_text, name)

            if response is None and any(
                word in normalize(user_text) for word in EXIT_KEYWORDS
            ):
                print(greetings.build_farewell(name))
                break

            if response is not None:
                print(f"Assistant: {response}" if not response.startswith("Assistant:") else response)

        except KeyboardInterrupt:
            print(f"\n{greetings.build_farewell(name)}")
            break
        except Exception as error:
            print(f"Assistant: Oops, something went wrong ({error}). Let's keep going.")


if __name__ == "__main__":
    main()

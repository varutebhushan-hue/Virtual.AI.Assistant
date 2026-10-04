import random

LOWER_BOUND = 1
UPPER_BOUND = 20
MAX_ATTEMPTS = 5


def play_guessing_game():
    secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)
    attempts_left = MAX_ATTEMPTS

    print(
        f"Assistant: I'm thinking of a number between {LOWER_BOUND} "
        f"and {UPPER_BOUND}. You have {MAX_ATTEMPTS} tries."
    )

    while attempts_left > 0:
        guess_text = input(f"Guess a number ({attempts_left} tries left): ").strip()

        try:
            guess = int(guess_text)
        except ValueError:
            print("Assistant: That's not a valid number — try again.")
            continue

        attempts_left -= 1

        if guess == secret_number:
            print(f"Assistant: You got it! The number was {secret_number}. Well done!")
            return
        elif guess < secret_number:
            print("Assistant: Higher!")
        else:
            print("Assistant: Lower!")

    print(f"Assistant: Out of tries! The number was {secret_number}. Better luck next time!")

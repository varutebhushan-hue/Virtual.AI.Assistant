# Mini Alexa — Virtual AI Assistant

A text-based, rule-based virtual assistant that runs entirely offline in a
terminal. Built for the Nexbridge Technologies AI Internship Program
(Project 1 — see the accompanying PRD).

No external datasets, APIs, or ML/DL frameworks are used — only the Python
standard library (`random`, `datetime`).

## Requirements

- Python 3.8 or newer
- No internet connection needed
- No third-party packages to install

## Setup & Run

```bash
cd virtual-ai-assistant
python main.py
```

You'll be greeted and asked for your name, then you can start typing commands.

## Available Commands

| Command | What it does |
|---|---|
| `time` | Shows the current time |
| `date` | Shows the current date |
| `calculate <num> <op> <num>` | Does a calculation, e.g. `calculate 12 + 8` |
| `joke` | Tells a random joke |
| `quote` | Shares a random motivational quote |
| `fact` | Shares a random fact |
| `game` | Plays a number guessing game (1–20, 5 tries) |
| `recommend` | Recommends an activity based on the time of day (rule-based demo) |
| `perceptron` | Runs a simplified single-neuron (perceptron) calculation |
| `help` | Lists all commands |
| `exit` / `quit` / `bye` | Ends the session |

## Project Structure

```
virtual-ai-assistant/
├── main.py             # Entry point; runs the input/route/respond loop
├── greetings.py         # Greeting logic and name capture
├── datetime_utils.py     # Date and time reporting
├── calculator.py         # Arithmetic parsing and calculation
├── content.py             # Quote/joke/fact lists and random selection
├── game.py                 # Number guessing game
├── ai_concepts.py          # Rule-based recommendation + perceptron demo
├── help_menu.py             # Formats and prints the help text
└── README.md
```

## Example Session

```
Assistant: Hi! I'm Mini Alexa. What's your name?
You: Priya
Assistant: Nice to meet you, Priya! Type 'help' to see what I can do.

You: calculate 12 + 8
Assistant: The result is 20

You: calculate 5 / 0
Assistant: I can't divide by zero — try a different number.

You: joke
Assistant: Why did the developer go broke? Because they used up all their cache.

You: exit
Assistant: Goodbye, Priya! Have a great day.
```

## Notes on AI/ML/DL Concepts

- **Rule-based system**: the entire command router in `main.py` is a set of
  explicit if/elif rules mapping keywords to responses.
- **`recommend` command**: a stand-in for a simple classifier — it maps one
  input feature (the current hour) to one of several predicted categories.
- **`perceptron` command**: demonstrates the building block of a neural
  network — inputs, fixed weights, a bias, a step activation function, and
  an output — with no training or external library involved.

See the PRD (sections 19–21) for the full mapping of concepts to code.

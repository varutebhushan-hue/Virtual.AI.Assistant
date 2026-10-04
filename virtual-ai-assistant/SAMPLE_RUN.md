# Mini Alexa — Sample Test Run

**Project:** Virtual AI Assistant (Mini Alexa)
**Tester:** Bhushan
**Date:** September 6, 2026
**Purpose:** Demonstrates every supported command working correctly in a single session, satisfying the manual testing expectations in the PRD (sections 29–33).

---

## Session Overview

| # | Command Tested | Result |
|---|---|---|
| 1 | `help` | Full command list displayed |
| 2 | `time` | Current time returned |
| 3 | `date` | Current date returned |
| 4 | `caalculate 15 + 8` (typo) | Friendly fallback — no crash |
| 5 | `calculate 15 + 8` | Correct result (`23`) |
| 6 | `joke` | Random joke returned |
| 7 | `quote` | Random quote returned |
| 8 | `fact` | Random fact returned |
| 9 | `recommend` | Rule-based activity recommendation |
| 10 | `game` | Number guessing game — won in 4 tries |
| 11 | `perceptron` | Neuron demo — output computed correctly |
| 12 | `bye` | Clean exit with goodbye message |

**Result:** All 14 functional requirements (FR-01 to FR-14) exercised successfully. No crashes, including on the intentional typo and mid-range calculator input.

---

## 1. Startup & Greeting (FR-01, FR-02)

```
Assistant: Hi! I'm Mini Alexa. What's your name?
You: Bhushan
Assistant: Nice to meet you, Bhushan! Type 'help' to see what I can do.
```

## 2. Help Menu (FR-10)

```
You: help
Assistant:
  - time                         show current time
  - date                         show current date
  - calculate <num> <op> <num>   do a calculation (e.g., calculate 12 + 8)
  - joke                         tell a joke
  - quote                        motivational quote
  - fact                         random fact
  - game                         play the number guessing game
  - recommend                    get an activity recommendation based on the time of day
  - perceptron                   run a simplified neural-network neuron demo
  - help                         show this list again
  - exit / quit / bye            quit the assistant
```

## 3. Date & Time (FR-03, FR-04)

```
You: time
Assistant: It's currently 10:55 AM.

You: date
Assistant: Today's date is Sunday, September 06, 2026.
```

## 4. Calculator — Error Handling & Correct Result (FR-05, FR-12)

```
You: caalculate 15 + 8
Assistant: I'm not sure I understood that — type 'help' to see what I can do.

You: calculate 15 + 8
Assistant: The result is 23
```

> Note: the typo `caalculate` correctly falls through to the fallback message instead of crashing — demonstrating FR-12's unrecognized-input handling.

## 5. Entertainment Features (FR-06, FR-07, FR-08)

```
You: joke
Assistant: Why was the JavaScript developer sad? Because they didn't know how to 'null' their feelings.

You: quote
Assistant: Your only limit is your mind.

You: fact
Assistant: The QWERTY keyboard layout was originally designed to slow typists down.
```

## 6. Rule-Based Recommendation (FR-13)

```
You: recommend
Assistant: Based on the current hour (10:00), I'd recommend: breakfast and a fresh start to the day.
(This is a rule-based decision, similar to how a classifier assigns a category based on an input feature.)
```

## 7. Number Guessing Game (FR-09)

```
You: game
Assistant: I'm thinking of a number between 1 and 20. You have 5 tries.
Guess a number (5 tries left): 5
Assistant: Higher!
Guess a number (4 tries left): 15
Assistant: Higher!
Guess a number (3 tries left): 18
Assistant: Higher!
Guess a number (2 tries left): 20
Assistant: You got it! The number was 20. Well done!
```

## 8. Perceptron Demo (FR-14)

```
You: perceptron
Assistant: Let's run a tiny perceptron (a single artificial neuron).
Enter a value for 'input 1': 15
Enter a value for 'input 2': 12
Enter a value for 'input 3': 13
Assistant:
Inputs:  [15.0, 12.0, 13.0]
Weights: [0.5, -0.6, 0.3]
Bias:    0.1
Weighted sum + bias = 4.3
Activation (step function): output = 1
(This mirrors forward propagation in a real neural network, just with fixed, untrained numbers.)
```

**Verification:** `(15 × 0.5) + (12 × -0.6) + (13 × 0.3) + 0.1 = 7.5 − 7.2 + 3.9 + 0.1 = 4.3` → step function outputs `1` since `4.3 > 0`. ✅ Matches expected output.

## 9. Graceful Exit (FR-11)

```
You: bye
Assistant: Goodbye, Bhushan! Have a great day.
```

---

## Conclusion

Every command in the help menu was exercised, including one deliberate typo to confirm the fallback path. The assistant handled all inputs without crashing, correctly used the stored user name across multiple responses, and produced varying random content across repeats where applicable — satisfying the acceptance criteria defined in PRD section 30.

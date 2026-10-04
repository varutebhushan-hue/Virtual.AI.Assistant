from datetime_utils import get_current_hour


def recommend_activity(hour=None):
    if hour is None:
        hour = get_current_hour()

    if 5 <= hour < 11:
        activity = "breakfast and a fresh start to the day"
    elif 11 <= hour < 14:
        activity = "lunch and a short break"
    elif 14 <= hour < 18:
        activity = "some focused work or study"
    elif 18 <= hour < 22:
        activity = "dinner and time to unwind"
    else:
        activity = "rest — it's getting late"

    return (
        f"Based on the current hour ({hour}:00), I'd recommend: {activity}.\n"
        f"(This is a rule-based decision, similar to how a classifier "
        f"assigns a category based on an input feature.)"
    )


def _get_numeric_inputs(prompt_labels):
    values = []
    for label in prompt_labels:
        raw = input(f"Enter a value for '{label}': ").strip()
        try:
            values.append(float(raw))
        except ValueError:
            print(f"Assistant: '{raw}' isn't a number — using 0 instead.")
            values.append(0.0)
    return values


def perceptron_demo():
    print("Assistant: Let's run a tiny perceptron (a single artificial neuron).")
    labels = ["input 1", "input 2", "input 3"]
    inputs = _get_numeric_inputs(labels)

    weights = [0.5, -0.6, 0.3]
    bias = 0.1

    weighted_sum = sum(i * w for i, w in zip(inputs, weights)) + bias

    output = 1 if weighted_sum > 0 else 0

    explanation = (
        f"\nInputs:  {inputs}\n"
        f"Weights: {weights}\n"
        f"Bias:    {bias}\n"
        f"Weighted sum + bias = {round(weighted_sum, 3)}\n"
        f"Activation (step function): output = {output}\n"
        f"(This mirrors forward propagation in a real neural network, "
        f"just with fixed, untrained numbers.)"
    )

    return explanation

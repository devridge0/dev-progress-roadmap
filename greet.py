# greet.py
# Simple script to practice commits and branching


def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}! Welcome to Git practice. Have a great day!"


def farewell(name):
    return f"Goodbye, {name}! See you next time."


if __name__ == "__main__":
    name = input("What's your name?")
    print(f"Hello, {name}! Welcome to our project")
    print(greet(name))

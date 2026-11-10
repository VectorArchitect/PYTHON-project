# Rock, Paper, Scissors

A beginner-friendly command-line Rock, Paper, Scissors game written in Python. The computer selects a choice randomly, and the player enters `rock`, `paper`, or `scissors`.

## Requirements

- Python 3.8 or later
- No third-party packages are required.

## Run

```bash
python "Rock, Paper, Scissors game.py"
```

Choices are case-insensitive and surrounding whitespace is ignored. Invalid input is reported without crashing the game.

## Run tests

```bash
python -m unittest discover -s tests -v
```

The tests cover all three winning combinations, draws, losses, input normalization, and invalid choices.

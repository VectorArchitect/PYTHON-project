import random

CHOICES = ("rock", "paper", "scissors")
WINS_OVER = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def decide_winner(user_choice, computer_choice):
    """Return the outcome for two choices, validating both inputs."""
    user_choice = str(user_choice).strip().lower()
    computer_choice = str(computer_choice).strip().lower()

    if user_choice not in WINS_OVER:
        raise ValueError("Choose rock, paper, or scissors.")
    if computer_choice not in WINS_OVER:
        raise ValueError("Computer choice must be rock, paper, or scissors.")

    if user_choice == computer_choice:
        return "Draw !"
    if WINS_OVER[user_choice] == computer_choice:
        return "YOU WIN !"
    return "YOU LOSE !"


def play():
    computer_choice = random.choice(CHOICES)
    user_choice = input("Enter your choice (rock/paper/scissors): ")

    try:
        outcome = decide_winner(user_choice, computer_choice)
    except ValueError:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return

    print(f"You: {user_choice.strip().lower()} ; Computer: {computer_choice}")
    print(outcome)


if __name__ == "__main__":
    play()

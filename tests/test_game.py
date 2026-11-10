import importlib.util
import unittest
from pathlib import Path

GAME_PATH = Path(__file__).resolve().parents[1] / "Rock, Paper, Scissors game.py"
SPEC = importlib.util.spec_from_file_location("rock_paper_scissors", GAME_PATH)
GAME = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GAME)


class DecideWinnerTests(unittest.TestCase):
    def test_draw(self):
        self.assertEqual(GAME.decide_winner("rock", "rock"), "Draw !")

    def test_rock_beats_scissors(self):
        self.assertEqual(GAME.decide_winner("rock", "scissors"), "YOU WIN !")

    def test_paper_beats_rock(self):
        self.assertEqual(GAME.decide_winner("paper", "rock"), "YOU WIN !")

    def test_scissors_beats_paper(self):
        self.assertEqual(GAME.decide_winner("scissors", "paper"), "YOU WIN !")

    def test_losing_choice(self):
        self.assertEqual(GAME.decide_winner("rock", "paper"), "YOU LOSE !")

    def test_normalizes_case_and_whitespace(self):
        self.assertEqual(GAME.decide_winner(" ROCK ", "Scissors"), "YOU WIN !")

    def test_rejects_invalid_user_choice(self):
        with self.assertRaises(ValueError):
            GAME.decide_winner("lizard", "rock")

    def test_rejects_invalid_computer_choice(self):
        with self.assertRaises(ValueError):
            GAME.decide_winner("rock", "invalid")


if __name__ == "__main__":
    unittest.main()

import pytest

from hangman import Hangman

def test_initial_values():
    game = Hangman("vaca")
    assert game.word == "VACA"
    assert game.number_of_incorrect_guesses == 0
    assert game.status == "in progress"

def test_incorrect_character():
    game = Hangman("vaca")
    assert game.word == "VACA"
    assert game.number_of_incorrect_guesses == 0
    guess = game.guess("0")
    assert game.number_of_incorrect_guesses == 0
    assert guess == "incorrect"

def test_incorrect_guess():
    game = Hangman("vaca")
    guess = game.guess("Z")
    assert game.number_of_incorrect_guesses == 1
    assert "Z" in game.incorrect_guesses
    assert guess == "incorrect"

def test_lower_letter_to_capital():
    game = Hangman("vaca")
    guess = game.guess("z")
    assert "Z" in game.incorrect_guesses

def test_incorrect_guess():
    game = Hangman("vaca")
    guess = game.guess("Z")
    assert game.number_of_incorrect_guesses == 1
    assert "Z" in game.incorrect_guesses
    assert guess == "incorrect"

def test_incorrect_duplicate_guess():
    game = Hangman("vaca")
    guess = game.guess("Z")
    assert game.number_of_incorrect_guesses == 1
    guess = game.guess("Z")
    assert game.number_of_incorrect_guesses == 1
    assert guess == "duplicate"

def test_correct_guess():
    game = Hangman("vaca")
    guess = game.guess("V")
    assert "V" in game.correct_guesses
    assert game.number_of_incorrect_guesses == 0
    assert guess == "correct"

def test_correct_duplicate_guess():
    game = Hangman("vaca")
    guess = game.guess("V")
    guess = game.guess("V")
    assert guess == "duplicate"

def test_custom_max_errors():
    game = Hangman("vaca")
    assert game.max_errors == 5

    game = Hangman("vaca", 1)
    assert game.max_errors == 1

def test_game_over():
    game = Hangman("vaca", 1)
    guess = game.guess("Z")
    assert game.status == "game over"

def test_guessed():
    game = Hangman("va", 1)
    guess = game.guess("v")
    assert game.number_of_guessed == 1

def test_multiple_guessed():
    game = Hangman("vaa", 1)
    guess = game.guess("a")
    assert game.number_of_guessed == 2

def test_same_answer_count_once():
    game = Hangman("va", 1)
    guess = game.guess("a")
    assert game.number_of_guessed == 1
    guess = game.guess("a")
    assert game.number_of_guessed == 1

def test_win():
    game = Hangman("va", 1)
    guess = game.guess("v")
    guess = game.guess("a")
    assert game.status == "win"

    game = Hangman("vaca", 1)
    guess = game.guess("v")
    guess = game.guess("a")
    guess = game.guess("c")
    assert game.status == "win"

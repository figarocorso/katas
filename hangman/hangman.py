class Hangman:
    def __init__(self, word, max_errors=5):
        self.word = word.upper()
        self.number_of_incorrect_guesses = 0
        self.number_of_guessed = 0
        self.incorrect_guesses = []
        self.correct_guesses = []
        self.max_errors = max_errors

    @property
    def status(self):
        if self.number_of_guessed == len(self.word):
            return "win"

        if self.number_of_incorrect_guesses < self.max_errors:
            return "in progress"

        return "game over"

    def guess(self, letter):
        letter = letter.upper()

        if not letter.isalpha():
            return "incorrect"

        if letter in self.incorrect_guesses or letter in self.correct_guesses:
            return "duplicate"

        if letter not in self.word:
            self.number_of_incorrect_guesses += 1
            self.incorrect_guesses.append(letter)
            return "incorrect"

        if letter in self.word:
            self.correct_guesses.append(letter)
            self.number_of_guessed += self.word.count(letter)
            return "correct"

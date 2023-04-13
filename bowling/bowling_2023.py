class Game:

    def __init__(self):
        self.rolls = []

    def score(self):
        frame_first_roll = 0
        score = 0
        while frame_first_roll <= len(self.rolls) - 2:
            if self.rolls[frame_first_roll] == 10:
                score += self.rolls[frame_first_roll] + self.rolls[frame_first_roll + 1] + self.rolls[frame_first_roll + 2]
                frame_first_roll += 1
                continue

            if self.rolls[frame_first_roll] + self.rolls[frame_first_roll + 1] == 10:
                score += self.rolls[frame_first_roll] + self.rolls[frame_first_roll + 1] + self.rolls[frame_first_roll + 2]
                frame_first_roll += 2
                continue

            score += self.rolls[frame_first_roll] + self.rolls[frame_first_roll + 1]
            frame_first_roll += 2

        return score

    def roll(self, pins):
        self.rolls.append(pins)

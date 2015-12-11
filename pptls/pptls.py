class PPTLS:
    def check_winner(self, first_choice, second_choice):
        first_choice = first_choice.lower()
        second_choice = second_choice.lower()

        winner = {
            'rock': ['lizard', 'scissors'],
            'scissors': ['paper', 'lizard'],
            'paper': ['rock', 'spock'],
            'spock': ['scissors', 'rock'],
            'lizard': ['paper', 'spock'],
        }

        if second_choice == first_choice:
            return 0

        if second_choice in winner[first_choice]:
            return 1

        return 2

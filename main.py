import random

from art import logo


class Blackjack:
    def __init__(self):
        """Initialize the Blackjack game with default values and start the game."""
        self.player_total = 0
        self.computer_total = 0
        self.cards = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10,
            "Ace": [1, 11],
        }
        self.play()
        self.play_again()

    def deal_card(self, computer_turn=False):
        """
        Deal a card from the deck and return its value.
        If it's the computer's turn and the drawn card is an Ace, choose 11 as its value if the total is less than 11.
        """
        card_name = random.choice(list(self.cards.keys()))
        card_value = self.cards[card_name]
        if card_name == "Ace":
            if computer_turn and self.computer_total < 11:
                card_value = 11
            else:
                try:
                    card_value = int(
                        input("Ace Drawn! Do you want to use it as 1 or 11? ")
                    )
                except ValueError:
                    print("Invalid input. Using Ace as 1.")
                    card_value = 1
        return card_value

    def player_turn(self):
        """Manage the player's turn, allowing them to hit or stand."""
        self.player_total = self.deal_card() + self.deal_card()
        print(f"Player's starting total: {self.player_total}")
        while True:
            choice = input("Hit or Stand? 'h/s' ").lower()
            if choice == "h":
                drawn_card = self.deal_card()
                self.player_total += drawn_card
                print(f"You draw: {drawn_card}. Total: {self.player_total}")
                if self.player_total > 21:
                    print("You Bust!")
                    return self.player_total
                elif self.player_total == 21:
                    print("Player Gets Blackjack!")
                    return self.player_total
            else:
                print(f"Player stands with total: {self.player_total}")
                return self.player_total

    def computer_turn(self):
        """Manage the computer's turn, drawing cards as per Blackjack rules."""
        self.computer_total = self.deal_card(computer_turn=True) + self.deal_card(
            computer_turn=True
        )
        print(f"Computer's starting total: {self.computer_total}")
        while self.computer_total < 17:
            drawn_card = self.deal_card(computer_turn=True)
            self.computer_total += drawn_card
            print(f"Computer draws: {drawn_card}. Total: {self.computer_total}")
            if self.computer_total > 21:
                print("Computer Busts!")
                return self.computer_total
            elif self.computer_total == 21:
                print("Computer Gets Blackjack!")
                return self.computer_total
        print(f"Computer stands with total: {self.computer_total}")
        return self.computer_total

    def declare_winner(self):
        """Determine the winner based on the final card totals."""
        if self.player_total == 21:
            print("\nPlayer Gets Blackjack!")
        elif self.computer_total == 21:
            print("\nComputer Gets Blackjack!")
        elif self.player_total > 21:
            print("\nPlayer Busts! Computer Wins!")
        elif self.computer_total > 21:
            print("\nComputer Busts! Player Wins!")
        elif self.player_total > self.computer_total:
            print("\nPlayer Wins!")
        elif self.computer_total > self.player_total:
            print("\nComputer Wins!")
        else:
            print("\nDraw!")
        return self.play_again()

    def play(self):
        """Play a full round of the game."""
        print(logo)
        self.player_total = self.player_turn()
        self.computer_total = self.computer_turn()
        result = self.declare_winner()
        print(result)

    def play_again(self):
        """Ask the player if they want to play another round."""
        while True:
            choice = input("Play again? 'y/n'  ").lower()
            if choice == "y":
                return self.play()
            elif choice == "n":
                return "Thanks for playing!"
            else:
                print("Invalid input.")


game = Blackjack()
game.play()

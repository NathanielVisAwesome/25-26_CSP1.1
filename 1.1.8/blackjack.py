import random

# Deck and card values
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


# Functions
def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]


def calculate_hand(hand):
    total = sum(values[card[0]] for card in hand)
    aces = sum(1 for card in hand if card[0] == 'A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


def display_hand(hand, hidden=False):
    if hidden:
        print(f"Dealer's Hand: [{hand[0][0]} of {hand[0][1]}, Hidden]")
    else:
        print(', '.join(f"{rank} of {suit}" for rank, suit in hand))


# Game loop
def blackjack():
    deck = create_deck()
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Welcome to Blackjack!\n")

    # Show initial hands
    display_hand(dealer_hand, hidden=True)
    display_hand(player_hand)
    print(f"Your total: {calculate_hand(player_hand)}\n")

    # Player turn
    while True:
        move = input("Do you want to [H]it or [S]tand? ").lower()
        if move == 'h':
            player_hand.append(deck.pop())
            display_hand(player_hand)
            total = calculate_hand(player_hand)
            print(f"Your total: {total}\n")
            if total > 21:
                print("You busted! Dealer wins.")
                return
        elif move == 's':
            break
        else:
            print("Invalid input. Please enter H or S.")

    # Dealer turn
    print("\nDealer's turn:")
    display_hand(dealer_hand)
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        display_hand(dealer_hand)

    dealer_total = calculate_hand(dealer_hand)
    player_total = calculate_hand(player_hand)

    print(f"\nDealer's total: {dealer_total}")
    print(f"Your total: {player_total}\n")

    # Determine winner
    if dealer_total > 21:
        print("Dealer busted! You win!")
    elif dealer_total > player_total:
        print("Dealer wins!")
    elif dealer_total < player_total:
        print("You win!")
    else:
        print("It's a tie!")


# Run the game
if __name__ == "__main__":
    blackjack()

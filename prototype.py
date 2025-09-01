# Import Requirements
import random as rd

# Card Initialization
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9] * 4 + [10] * 16     # Assume A is 11

# Card Shuffling
rd.shuffle(cards)

# Players' Deck Initilization
playerDeck = []
dealerDeck = []

# Round Robin
for n in range(2):
    playerDeck.append(cards.pop())
    dealerDeck.append(cards.pop())

# Loop (Player's Turn)
playerTurn = True
while playerTurn:
    # Display Card
    print(f"Player's Deck: {playerDeck}, score: {sum(playerDeck)}")
    print(f"Dealer's Deck: {dealerDeck[:-1]}, score: {sum(dealerDeck[:-1])}")

    # Demand Input
    choice = input("take or pass? \n").lower()

    # Input switch
    match choice:
        case "take":
            playerDeck.append(cards.pop())
        case "pass":
            playerTurn = False
        case _:
            raise ValueError(f"Invalid Input: \"{choice}\". Only accepts \"take\" or \"pass\".")

# Dealer's Turn
while sum(dealerDeck) < 17:
    dealerDeck.append(cards.pop())

# Final Score Calculation
playerFinalScore = sum(playerDeck)
dealerFinalScore = sum(dealerDeck)

# Display Result
print("Final Result:")
print(f"Player: {playerDeck}, score: {playerFinalScore}")
print(f"Dealer: {dealerDeck}, score: {dealerFinalScore}")

# Game Conclusion
if playerFinalScore > 21:
    print("You busted.")
elif dealerFinalScore > 21:
    print("The dealer busted. You win.")
elif dealerFinalScore > playerFinalScore:
    print("You lose.")
elif dealerFinalScore == playerFinalScore:
    print("Draw.")
elif dealerFinalScore < playerFinalScore:
    print("You win.")
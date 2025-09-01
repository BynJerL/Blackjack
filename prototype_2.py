import random as rd

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9] * 4 + [10] * 16 
rd.shuffle(cards)

playerDeck, dealerDeck = [], []

for n in range(2):
    playerDeck.append(cards.pop())
    dealerDeck.append(cards.pop())

def compareScore(playerScore: int, dealerScore: int):
    if playerScore > 21 and dealerScore > 21:
        print("You went over. You lose 😔")
        return
    
    if playerScore > 21:
        print("You went over. You lose 😔")
    elif dealerScore > 21:
        print("Enemy went over. You win 😊")
    elif playerScore > dealerScore:
        print("You win 😃")
    elif playerScore == dealerScore:
        print("Draw 🙃")
    elif playerScore < dealerScore:
        print("You lose 😒")

def playerTurn():
    print(f"Player's Deck: {playerDeck}, score: {sum(playerDeck)}")
    print(f"Dealer's Deck: {dealerDeck[:-1]}, score: {sum(dealerDeck[:-1])}")

    choice = input("take or pass? \n").lower()

    match choice:
        case "take":
            playerDeck.append(cards.pop())
            if sum(playerDeck) > 21:
                return
            else:
                playerTurn()
        case "pass":
            return
        case _:
            raise ValueError(f"Invalid Input: \"{choice}\". Only accepts \"take\" or \"pass\".")

def dealerTurn():
    if sum(dealerDeck) < 17:
        dealerDeck.append(cards.pop())
    else:
        return

if __name__ == '__main__':
    playerTurn()
    dealerTurn()

    playerFinalScore = sum(playerDeck)
    dealerFinalScore = sum(dealerDeck)

    print("Final Result:")
    print(f"Player: {playerDeck}, score: {playerFinalScore}")
    print(f"Dealer: {dealerDeck}, score: {dealerFinalScore}")

    compareScore(playerFinalScore, dealerFinalScore)
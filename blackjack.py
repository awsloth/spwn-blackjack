import random

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q","K"]
suits = ["D", "C", "S", "H"]
values = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,
          "10":10, "J":10, "Q":10, "K":10}

deck = []
for suit in suits:
    for card in cards:
        deck.append(card+suit)

whole_deck = deck.copy()

def get_cards():
    random.shuffle(deck)
    return deck.pop()

def eval_score(cards):
    cards = [x[:-1] for x in cards]
    score = sum([values[x] for x in cards])
    if "A" in cards and score <= 11:
        score += 10
    return score

while 1:
    deck = whole_deck.copy()
    user_cards = [get_cards() for _ in range(2)]
    dealer_cards =[get_cards() for _ in range(2)]

    print(user_cards)
    user_score = eval_score(user_cards)

    choice = input("Twist (0) or stick (1)? ")

    while choice == "0":
        user_cards.append(get_cards())
        print(user_cards)
        user_score = eval_score(user_cards)
        if user_score > 21:
            print("Bust")
            break
        choice = input("Twist (0) or stick (1)? ")

    dealer_score = eval_score(dealer_cards)
    while dealer_score < 16:
        dealer_cards.append(get_cards())
        dealer_score = eval_score(dealer_cards)
        
    user_score = eval_score(user_cards)
    print(user_cards, dealer_cards)
    print(user_score, dealer_score)
    
    if user_score > 21 and dealer_score > 21:
        print("Both bust, draw")
    elif user_score > 21:
        print("Bust, you lose")
    elif dealer_score > 21:
        print("Dealer bust, you win")
    elif user_score > dealer_score:
        print("Higher, you win")
    elif dealer_score > user_score:
        print("Lower, you lose")
    elif dealer_score == user_score:
        if len(dealer_cards) < len(user_cards):
            print("More cards, you win")
        elif len(user_cards) < len(dealer_cards):
            print("Less cards, you lose")
        elif len(user_cards) == len(dealer_cards):
            print("Draw")



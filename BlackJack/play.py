__author__ = 'nathan'

import random

class Player:

    def __init__(self, num):
        self.id = num
        self.hand = []
        self.in_game = True

    def __str__(self):
        return self.id


def print_deck(deck):
    for item in deck:
        string=""
        suit = ""
        if item % 4 == 0:
            suit = "Hearts"
        elif item % 4 == 1:
            suit = "Clubs"
        elif item % 4 == 2:
            suit = "Diamonds"
        elif item % 4 == 3:
            suit = "Spades"
        face = (item%13)+2
        if face == 14:
            print(item, ":", "Ace of " + suit)
        elif face == 11:
            print(item, ":", "Jack of " + suit)
        elif face == 12:
            print(item, ":", "Queen of " + suit)
        elif face == 13:
            print(item, ":", "King of " + suit)
        else:
            print(item, ":", face, "of " + suit)


def show_hand(person, game_over):
    string=""
    n = 0
    for item in person.hand:
        suit = ""
        if item % 4 == 0:
            suit = "Hearts"
        elif item % 4 == 1:
            suit = "Clubs"
        elif item % 4 == 2:
            suit = "Diamonds"
        elif item % 4 == 3:
            suit = "Spades"

        if person.id != USER and not game_over:
            if n == 0:
                string += "?, "
                n = 1
            else:
                string+= str(((item % 13) + 2))+" of "+suit +", "
        else:
            string+= str(((item % 13) + 2))+" of "+suit +", "
    return string[:-2]


def sum_hand(person,game_over):
    ACE = [12,25,38,51]
    if person.id == USER or game_over:
        hand_value = 0
        for card in person.hand:
            points =  ((card % 13) + 2)
            if points > 13:
                hand_value += 11
            elif points > 10:
                hand_value += 10
            else:
                hand_value += points
        #print(hand_value, "Before Ace(s)")
        for item in ACE:
            if item in person.hand and hand_value > 21:
                #print("YOU HAVE AN ACE")
                hand_value -= 10
        #print(hand_value, "After Ace(s)")
        return hand_value
    return "?"


def hit(deck, person):
    new_card = deck.pop()
    person.hand.append(new_card)
    #return hand


def stand(person):
    person.in_game = False
    #return in_game


def double_down():
    pass


def split():
    pass


def surrender():
    pass


def deal(deck,players):
    for person in all_players:
        hit(deck,person)
        hit(deck, person)


def view(players,game_over):
    for person in players:
        if person.id != DEALER:
            print("Player "+ str(person.id) + "\tHand value", sum_hand(person,game_over), "\tHand:", show_hand(person,game_over))
        else:
            print("Dealer    \tHand value", sum_hand(person,game_over), "\tHand:", show_hand(person,game_over))


def play(deck,players):
    player_num = 0

    #Give every player a turn.
    while player_num < len(players):
        #If it's the user's turn
        #Make sure user didn't bust.
        if sum_hand(players[player_num],True) < 22:
            if players[player_num].id == USER:

                view(players,False)
                action = ""

                #User decides what to do.
                while action.lower() != "hit" and \
                        action.lower() != "stand" and \
                        action.lower() != "double down" and \
                        action.lower() != "split" and \
                        action.lower() != "surrender":
                    action = str(input("What would you like to do?"))
                if action.lower() == 'hit':
                    hit(deck,players[player_num])
                elif action.lower() == 'stand':
                    stand(players[player_num])
                    player_num += 1
                elif action.lower() == 'double down':
                    double_down()
                    player_num += 1
                elif action.lower() == 'split':
                    split()
                    player_num += 1
                elif action.lower() == 'surrender':
                    surrender()
                    player_num += 1

            else:
                #Automated player plays
                #stand(players[player_num])
                if random.randint(0,22) > sum_hand(players[player_num],True):
                    hit(deck,players[player_num])
                else:
                    stand(players[player_num])
                player_num += 1

        #Over 21 points.
        else:
            print("Player "+str(player_num)+" BUSTED")
            stand(players[player_num])
            player_num += 1
            print(player_num)

def players_playing(players):
    x = False
    for person in players:
        if person.in_game == True:
            x = True
    return x


def winning(players):
    dealer_score = sum_hand(players[DEALER],True)
    for person in players:
        if person.id != DEALER:
            player_score = sum_hand(person,True)
            if  dealer_score < player_score <= 21:
                if person.id == USER:
                    print("You beat the dealer with a score of "+ str(player_score)+"!")
                else:
                    print("Player " + str(person.id)+ " beat the dealer with a score of " + str(player_score) + "!")
            else:
                if person.id == USER:
                    busted = ""
                    if player_score > 21:
                        busted = "You busted! "
                    print(busted + "Better luck next time!")
                else:
                    print("The dealer beat Player " + str(person.id))

if __name__ == '__main__':
    deck = []
    for i in range(0, 52):
        deck.append(i)
    print_deck(deck)
    input("This is the deck.")
    random.shuffle(deck)

    #Game info from user.
    num_decks = int(input("How many decks do you want to play with?"))
    deck *= num_decks
    num_players = int(input("How many players are there?"))

    DEALER = num_players
    USER = 0

    #Setting up players and hands.
    x = 0
    all_players = []
    print("CREATING PLAYERS")
    while x < num_players + 1:
        person = Player(x)
        all_players.append(person)
        x += 1
    print("DEALING")
    deal(deck, all_players)
    x = players_playing(all_players)

    #Play Game
    play(deck,all_players)

    print("GAME OVER")
    view(all_players,True)
    winning(all_players)

__author__ = 'nathan'

import random

class Player:

    def __init__(self, num):
        self.id = num
        self.hand = []
        self.in_game = True
        self.busted = False

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
        
        face=((item%13)+2)
        if face == 14:
            face = "Ace"
        elif face == 13:
            face = "King"
        elif face == 12:
            face = "Queen"
        elif face == 11:
            face = "Jack"

        if person.id != USER and not game_over:
            if n == 0:
                string += "?, "
                n = 1
            else:
                string+= str(face)+" of "+ suit +", "
        else:
            string+= str(face)+" of "+ suit +", "
    return string[:-2]


def sum_hand(person,game_over):
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
        #for item in ACE:
        #    if item in person.hand and hand_value > 21:
        #        #You have an ace, and would bust if it counts as 11 points.
        num_aces = any_aces(person)
        while num_aces > 0 and hand_value > 21:
            hand_value -= 10
            num_aces -= 1
        return hand_value
    return "?"


def hit(deck, person):
    new_card = deck.pop()
    person.hand.append(new_card)
    if (sum_hand(person,True) > 21):
        #print("BUST")
        person.busted = True
        person.in_game = False
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

def any_aces(player):
    ACE = [12,25,38,51]
    return len(set(ACE).intersection(player.hand))


def play(deck,players):
    player_num = 0

    #Give every player a turn.
    while player_num < len(players):
        #print("Take a turn, player",player_num)
        #Make sure the player didn't bust.
        #if sum_hand(players[player_num],True) < 22:
        if((players[player_num].in_game)):
            #print("Player is in game.")
            #User's turn.
            if players[player_num].id == USER:
                #print("Player is user")
                view(players,False)
                action = ""
            
                #User decides what to do.
                while action.lower() != "hit" and \
                        action.lower() != "stand" and \
                        action.lower() != "double down" and \
                        action.lower() != "split" and \
                        action.lower() != "surrender":
                    action = str(input("What would you like to do? You can 'hit' or 'stand'. "))
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
            #Dealer follows soft-hit rules
            #print("Dealer is player number",DEALER)
            #Dealer's turn.
            elif players[player_num].id==DEALER:
                #print("Player is dealer")
                score=(sum_hand(players[player_num],True))
                #print("Dealer is playing.")
                if score < 17:
                    hit(deck,players[player_num])
                    #print("Dealer hit with score less than 17")
                elif score == 17:
                    num_aces = any_aces(players[player_num])
                    if num_aces > 0:
                        hit(deck,players[player_num])
                        #print("Dealer hit with a soft 17")
                    else:
                        stand(players[player_num])
                else:
                    stand(players[player_num])
                    player_num += 1
                    #print("Dealer stands")
            #Other player's turn.
            else:
                #print("PLayer is bot")
                #Automated player plays
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
            #print(player_num)


def players_playing(players):
    """
    Determines if any players are currently playing.
    """
    x = False
    for person in players:
        if person.in_game == True:
            x = True
    return x


def winning(players):
    """
    Prints out the result of each player vs Dealer.
    """
    dealer_score = sum_hand(players[DEALER],True)
    #print("Is Dealer still in?",players[DEALER].busted)
    #print(players[DEALER].hand)
    for person in players:
        if person.id != DEALER:
            #print("Is player still in?",person.busted)
            player_score = sum_hand(person,True)
            if (players[DEALER].busted and not person.busted):
                print("PLayer",str(person.id),"beat the dealer, who busted!")
            elif  dealer_score < player_score <= 21:
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
    play_again = 0
    while play_again == 0:
        #Set up deck.
        deck = []
        for i in range(0, 52):
            deck.append(i)
        #print_deck(deck)
        #print("This is the deck.")
        random.shuffle(deck)
    
        #Game info from user.
        num_decks = 0
        num_players = -1
        while num_decks < 1:
            num_decks = int(input("How many decks do you want to play with? "))
        deck *= num_decks
        while num_players < 0:
            num_players = int(input("How many other players are there? ")) + 1
    
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
        #View results (Score, Hand, won/lost to delaer.)
        view(all_players,True)
        winning(all_players)
        #Play again?
        again =""
        while (again.lower()!="y" and again.lower()!="n"):
            again = input("Would you like to play again? (y/n)")
        if again.lower() == "y":
            play_again = 0
        else:
            play_again = 1

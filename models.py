import random


class Game:
    def __init__(self, cash=200):
        self.deck = Deck()
        self.player = Player(cash, self.deck)
        self.System = System()
        self.is_blackjack = False
        self.beginning = True

    def deal(self):
        print("Here is how much cash you have: " + str(self.player.cash))
        self.player.hit()
        self.player.hit()

    def show(self):
        print('You: %s ' % (self.player.current_hand.cards))

    def question_bet(self):
        bet_amount = 0
        while bet_amount <= 0:
            try:
                bet_amount = int(raw_input("Enter bet amount: "))
            except ValueError:
                print("Please input a number stoopid")
                bet_amount = 0
                continue
            if bet_amount > self.player.cash:
                print("You broke man, sorry")
                continue
            if bet_amount < 0:
                print("beep bop boop cannot compute. Please input valid number")
                continue
            if bet_amount == 0:
                print("nobody can be that scared :( gimme a number")
                continue

        print("Bet amount: " + str(bet_amount))
        return bet_amount

    def question_action(self):
        actions = ['h', 's', 'd']

        act = raw_input(
            "What will you do? (h: Hit | s: Stand | d: Double down): ")
        while act not in actions:
            print("Invalid response! Try again.")
            self.question_action()
        return act


class Player:
    def __init__(self, cash, deck):
        self.deck = deck
        self.cash = cash
        self.is_stand = False
        self.current_hand = Hand()
        self.busted = False

    def hit(self):
        new_card = self.deck.hit()
        self.current_hand.cards.append(new_card.value)

    def stand(self):
        self.is_stand = True

    def double(self):
        self.current_hand.bet *= 2
        self.hit()
        self.is_stand = True

    def send(self, action):
        action_dict = {'h': self.hit, 's': self.stand, 'd': self.double}
        action_dict[action]()

    def get_deck(self):
        return self.deck

    def reset(self):
        self.is_stand = False
        self.busted = False


class System:
    def __init__(self):
        self.hand_list = Hand()
        self.is_stand = False
        self.current_hand = self.hand_list
        self.busted = False

    def hit(self, deck):
        new_card = deck.hit()
        self.current_hand.cards.append(new_card.value)

    def play(self, deck):
        while (self.current_hand.points() < 17):
            self.hit(deck)
            self.show()
        return self.current_hand.points()

    def reset(self):
        self.is_stand = False
        self.busted = False

    def show(self):
        print('System: %s' % (self.current_hand.cards))


class Hand:
    def __init__(self):
        self.bet = 0
        self.cards = []

    def points(self):
        s = 0
        for card in self.cards:
            s += card
        return s


class Deck:
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.list_of_cards = self.cards()
        random.shuffle(self.list_of_cards)

    def cards(self):
        list_cards = []
        for suit in self.suits:
            for index, name in enumerate(self.names):
                list_cards.append(Card(suit, name, index))
        return list_cards

    def hit(self):
        if len(self.list_of_cards) < 10:
            print('There are less than 10 cards left. The deck has been reset')
            self.list_of_cards = self.cards()
            random.shuffle(self.list_of_cards)
        return self.list_of_cards.pop()

    def shuffle(self):
        random.shuffle(self.list_of_cards)


class Card:
    def __init__(self, suit, names, value):
        self.name = "{0} of {1}".format(suit, value+2)

        if value <= 8:
            self.value = value + 2
        else:
            self.value = 10


Game()

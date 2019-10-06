from models import *


def main(cash=200):
    game = Game(cash)
    reply = 'y'
    while reply == 'y':
        game.deal()
        game.player.bet = game.question_bet()
        hand = game.player.current_hand
        hand.bet = game.player.bet
        game.show()

        while(not game.player.busted and not game.player.is_stand):
            action = game.question_action()
            game.player.send(action)
            game.show()
            if hand.points() == 21:
                print("Blackjack! You win!")
                game.player.cash += (3 * hand.bet)
                print('Cash: %s' % (game.player.cash))
                game.is_blackjack = True
                break

            if hand.points() > 21:
                game.player.busted = True

        if not game.is_blackjack:
            if game.player.busted:
                print("You busted! You've now lost this hand! ")
                game.player.cash -= hand.bet

                print('Cash: %d' % (max(0, game.player.cash)))
            else:
                System_points = game.System.play(game.player.deck)
                if System_points > 21:
                    print("System busted! You win this hand!")
                    game.player.cash += hand.bet
                    print('Cash: %d' % (game.player.cash))
                elif System_points < hand.points():
                    print("You win this hand!")
                    game.player.cash += hand.bet
                    print('Cash: %d' % (game.player.cash))
                elif System_points == hand.points():
                    print("Bet returned!")
                else:
                    print("You lose this hand!")
                    game.player.cash -= hand.bet
                    print('Cash: %d' % max(0, game.player.cash))
        game.player.current_hand = Hand()
        game.player.reset()
        game.System.current_hand = Hand()
        game.System.reset()
        game.is_blackjack = False

        try:
            continuing = raw_input("Play again? [y] or [yes]: ")
            continuing = continuing.lower()
        except NameError:
            pass

        if continuing == 'y' or continuing == 'yes':
            if game.player.cash <= 0:
                print("Your money has been reset!")
                game.player.cash = 200
        else:
            reply = 'n'
            print('Thanks for playing!')


if __name__ == "__main__":
    try:
        cash = int(raw_input("how much cash do you want to have?: "))
    except:
        print("No input: default 200 cash")
        cash = 200
    main(cash)

# Basic Blackjack

## To run:

    python blackjack.py
    run on python version 2.7 created on 2.7.15

## How to play:

    The game is basic. Once the game starts, you either hit, double hit, or stand.
    The goal is to reach as close to 21 and below. Follow the prompt on the CLI.

## Design Choice:

    I chose to create classes for the Game, player, deck, system, card, and hand.
    The deck will have 52 cards, and it will reset after 42 cards have been played.
    I chose to make this a single player game because it is like the real life game.
    Very few module were used. Only random from python's standard library was used.

    The game is replayable, and your cash is kept track. Money will reset to your
    choice everytime the file is ran.

## Left out:

    I could have attatched the game to a backend in which kept track of different players
    through a basic login.
    I left out database tracking of money due to the scope of the project.
    In total: The project took about 2 hours.

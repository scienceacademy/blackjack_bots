# Blackjack Bot

The code in this repository lets you build and test Python bots to play Blackjack.

## How to play

To play a game, run the program using this command line syntax:

```bash
python blackjack_game.py bots/bot_human.py 1
```

This runs a game with `bot_human` playing `1` game (one shuffle through the deck).

## Bot Instructions

In the `bots/` folder are two bots you can look at to see how a bot should be formatted:

* `bot_bad.py` - This is a terrible bot that just randomly chooses what to do.
* `bot_human.py` - This bot lets you play as a human. It will ask you what you want to do.

The bot should follow these rules:

* Name your bot file `bot_<username>.py`
* Its class must be `Bot`.
* It must have a method called `get_decision()`, which will receive two arguments:
    * The dealer's up card
    * The player's hand.

The function must then decide what action to take, returning *only* one of the following strings: `"hit"`, `"stand"`, `"split"`, or `"double down"`.
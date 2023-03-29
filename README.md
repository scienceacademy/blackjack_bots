# Blackjack Bots

The code in this repository lets you build and test Python bots to play Blackjack.

To download this code in your CodeSpace, paste the following command in the Terminal window:

```bash
wget https://github.com/scienceacademy/blackjack_bots/archive/refs/tags/1.zip
unzip 1.zip
```

This will create a folder containing all the files listed above.

## How to play

To play a game, run the program using this command line syntax:

```bash
python blackjack_game.py bots/bot_human.py 1
```

This runs a game with the bot named `bot_human` playing `1` game (one shuffle through the deck).

At the end of the run of games, the program will print out a final score, showing its overall win/loss and per-hand average. You can use this score to evaluate how well your bot is doing.

## Bot Instructions

In the `bots/` folder are two example bots you can look at to see how a bot should be made:

* `bot_bad.py` - This is a terrible bot that just randomly chooses what to do.
* `bot_human.py` - This bot lets you play as a human. It will ask you what you want it to do.

The bot should follow these rules:

* Name your bot file `bot_<username>.py`
* Its class must be `Bot`.
* It must have a method called `get_decision()`, which will receive two arguments:
    * The dealer's up card, a `Card` object.
    * The player's hand, a list of `Card`s.
    * The dealer's previous hand, a list of `Card`s.

The function must then decide what action to take, returning *only* one of the following strings: `"hit"`, `"stand"`, `"split"`, or `"double down"`.

**If your bot returns an illegal move, such as doubling down on more than two cards, it will be treated as "stand".**

The rest is up to you. You can import libraries, make other functions, etc. as you need them to help your bot make the best choices.


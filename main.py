# starter bot refactored from Riddles Hackman python2 starter bot
import sys

from Bot.game import Game
from Bot.bot import Bot

def main():
    bot = Bot()
    game = Game()
    game.run(bot)

if __name__ == '__main__':
    main()

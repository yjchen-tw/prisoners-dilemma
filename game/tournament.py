# import random

from game import Game

import itertools
import player


class Tournament(object):

    def __init__(self, players):
        self.players = players
        self.num_of_rounds = 5

    def start_tournament(self):
        for player1, player2 in itertools.combinations(self.players, 2):
            for _ in range(self.num_of_rounds):
                game = Game(player1, player2)
                game.play()


if __name__ == '__main__':
    player1 = player.Player()
    player2 = player.Player()
    a = Tournament([player1, player2])
    a.start_tournament()

    print player1._payoff, player2._payoff

# import random

import itertools
from operator import attrgetter

import player

from game import Game

class Tournament(object):

    def __init__(self, players):
        self.players = players
        self.num_of_rounds = 20

    def start_tournament(self):
        for player1, player2 in itertools.combinations(self.players, 2):
            for _ in range(self.num_of_rounds):
                game = Game(player1, player2)
                game.play()

    def get_simulation_data(self):
        payoff_list = []
        name_list = []
        for i, player in enumerate(sorted(
                self.players, reverse=True, key=attrgetter('payoff'))):
            payoff_list.append({'data': [[i, player.payoff]], 'color': player.color})
            name_list.append([i, player.name])
        return {'payoff_list': payoff_list, 'name_list': name_list}


if __name__ == '__main__':
    player1 = player.Cooperator(2)
    player2 = player.TitForTatPlayer(3)
    player3 = player.Player(1)
    a = Tournament([player1, player2, player3])
    a.start_tournament()
    print a.get_simulation_data()

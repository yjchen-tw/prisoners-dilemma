
import random
import collections

COOPERATION = True
BETRAY = False


class Player(object):

    def __init__(self):
        self._payoff = 0
        self.game_record = collections.defaultdict(list)

    def play_against(self, opponent_id):
        ''' Default player randomly choose a stratgy '''
        return random.choice([COOPERATION, BETRAY])

    def increase_payoff(self, amount):
        self._payoff += amount

    def save_game_record(self, game):
        self.game_record['']


class Cooperator(Player):

    def play_against(self, opponent_id):
        return COOPERATION


class Betrayer(Player):

    def play_against(self, opponent_id):
        return BETRAY


class TitForTatPlayer(Player):

    def player_against(self, opponent_id):
        if opponent_id not in self.game_history:
            return COOPERATION
        else:
            return self.game_record[opponent_id][-1][0]

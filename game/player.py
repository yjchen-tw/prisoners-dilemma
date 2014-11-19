
import random
import collections

COOPERATION = True
BETRAY = False


class Player(object):
    color = 'blue'
    name_prefix = 'Random'

    def __init__(self, player_index=0):
        self.payoff = 0
        self.name = self.name_prefix + str(player_index)
        self.game_record = collections.defaultdict(list)

    def play_against(self, opponent_id):
        ''' Default player randomly choose a stratgy '''
        return random.choice([COOPERATION, BETRAY])

    def increase_payoff(self, amount):
        self.payoff += amount

    def save_game_record(self, opponent_id, strategies):
        self.game_record[opponent_id].append(strategies)


class Cooperator(Player):
    color = 'green'
    name_prefix = 'Cooperator'

    def play_against(self, opponent_id):
        return COOPERATION


class Betrayer(Player):
    color = 'red'
    name_prefix = 'Betrayer'

    def play_against(self, opponent_id):
        return BETRAY


class TitForTatPlayer(Player):
    color = 'yellow'
    name_prefix = 'Tit_for_tat'

    def play_against(self, opponent_id):
        if opponent_id not in self.game_record:
            return COOPERATION
        else:
            return self.game_record[opponent_id][-1][0]

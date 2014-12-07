
from player import COOPERATION, BETRAY


class Payoff(object):
    BETRAY = 5
    COOPERATION = 3
    BETRAY_EACH_OTHER = 1
    GET_BETRAYED = 0


class Game(object):

    def __init__(self, player1, player2):
        self.players = [player1, player2]

    def play(self):
        players = self.players
        strategies = [
            players[0].play_against(id(players[1])),
            players[1].play_against(id(players[0]))
        ]
        self.strategies = strategies
        # print strategies

        if strategies[0] == COOPERATION and strategies[1] == COOPERATION:
            for player in self.players:
                player.increase_payoff(Payoff.COOPERATION)
        elif strategies[0] == COOPERATION and strategies[1] == BETRAY:
            players[0].increase_payoff(Payoff.GET_BETRAYED)
            players[1].increase_payoff(Payoff.BETRAY)
        elif strategies[0] == BETRAY and strategies[1] == COOPERATION:
            players[0].increase_payoff(Payoff.BETRAY)
            players[1].increase_payoff(Payoff.GET_BETRAYED)
        else:
            for player in self.players:
                player.increase_payoff(Payoff.BETRAY_EACH_OTHER)

        self._send_record_to_players()

    def _send_record_to_players(self):
        strategies = self.strategies
        self.players[0].save_game_record(
            id(self.players[1]), (strategies[1], strategies[0]))
        self.players[1].save_game_record(
            id(self.players[0]), (strategies[0], strategies[1]))

import logging

from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import TournamentInfoForm
from .forms import FORM_FIELD_TO_PLAYER_OBJECT
from tournament import Tournament

LOGGER = logging.getLogger(__name__)


class GameSimulationView(FormView):
    template_name = 'simulation.html'
    form_class = TournamentInfoForm
    success_url = '/'

    def _append_label_for_legend(self, payoff_list):
        for player_type in FORM_FIELD_TO_PLAYER_OBJECT.values():
            for payoff in payoff_list:
                if payoff['color'] == player_type.color:
                    payoff['label'] = player_type.name_prefix
                    break

    def _generate_players(self, tournament_info):
        players = []
        for key, num in tournament_info.items():
            players.extend([FORM_FIELD_TO_PLAYER_OBJECT[key](i) for i in range(num)])
        return players

    def _run_simulation(self, players):
        tournament = Tournament(players)
        tournament.start_tournament()
        simulation_data = tournament.get_simulation_data()
        self._append_label_for_legend(simulation_data['payoff_list'])
        return simulation_data

    def form_valid(self, form):
        players = self._generate_players(form.cleaned_data)
        simulation_data = self._run_simulation(players)
        context = {'simulation_data': simulation_data, 'form': form}
        return render(self.request, 'simulation.html', context)

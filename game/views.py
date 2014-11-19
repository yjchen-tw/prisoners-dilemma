# Create your views here.
import logging

from django.shortcuts import render

LOGGER = logging.getLogger(__name__)

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect

from .forms import TournamentInfoForm
from .forms import FORM_FIELD_TO_PLAYER_OBJECT
from tournament import Tournament


class HelloView(View):

    def get(self, request):
        return HttpResponse("Hello world")


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

    def form_valid(self, form):
        form_data = form.cleaned_data
        LOGGER.info('{}'.format(form_data))
        players = []
        for key, num in form_data.items():
            players.extend([FORM_FIELD_TO_PLAYER_OBJECT[key](i) for i in range(num)])
        LOGGER.info('{}'.format(players))
        tournament = Tournament(players)
        tournament.start_tournament()
        simulation_data = tournament.get_simulation_data()
        self._append_label_for_legend(simulation_data['payoff_list'])
        LOGGER.info('{}'.format(simulation_data))
        context = {'simulation_data': simulation_data, 'form': form}
        return render(self.request, 'simulation.html', context)

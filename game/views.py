# Create your views here.
import logging

LOGGER = logging.getLogger(__name__)

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect

from .forms import TournamentInfoForm

class HelloView(View):

    def get(self, request):
        return HttpResponse("Hello world")


class GameSimulationView(FormView):
    template_name = 'simulation.html'
    form_class = TournamentInfoForm
    success_url = '/'

    def form_valid(self, form):
        form_data = form.cleaned_data
        LOGGER.info('{}'.format(form_data))
        return HttpResponseRedirect('')

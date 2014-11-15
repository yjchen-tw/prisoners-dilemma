# Create your views here.

from django.views.generic import TemplateView
from django.views.generic.base import View

from django.http import HttpResponse


class HelloView(View):

    def get(self, request):
        return HttpResponse("Hello world")

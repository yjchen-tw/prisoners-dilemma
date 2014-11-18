from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',

    url(r'^simulation/$', views.GameSimulationView.as_view()),

)

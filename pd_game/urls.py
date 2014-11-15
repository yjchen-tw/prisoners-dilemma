from django.conf.urls import patterns, include, url
from game.views import HelloView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pd_game.views.home', name='home'),
    url(r'^$', HelloView.as_view()),
    # url(r'^pd_game/', include('pd_game.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

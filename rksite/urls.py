from django.conf.urls import patterns, url
from rksite import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^projects/$', views.projects, name="projects"),
    url(r'^goals/$', views.goals, name="goals"),
    url(r'^thanks/$', views.thanks, name="thanks"),
)
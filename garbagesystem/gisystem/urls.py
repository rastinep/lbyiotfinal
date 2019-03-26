from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^campus/$', views.campus_overview, name='campus_overview'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^overview/$', views.overview, name='overview'),
    url(r'^hall/$', views.hall, name='hall'),
]

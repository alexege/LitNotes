from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^public$', views.index), 
    url(r'^$', views.public),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
]
from django.conf.urls import url

from . import views


app_name = 'library'
urlpatterns = [
    url(r'^index?', views.index, name='index'),
]

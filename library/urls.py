from django.conf.urls import url
from django.urls import include

from rest_framework.routers import DefaultRouter
from . import views


routerAPI = DefaultRouter()
routerAPI.register(r'books', views.BookViewSet, basename='books')
routerAPI.register(r'categories', views.CategoryViewSet, basename='categories')


app_name = 'library'
urlpatterns = [
    url(r'^api/', include(routerAPI.urls)),
]

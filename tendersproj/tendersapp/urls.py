from django.urls import path
from . import views

app_name = 'tendersapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('new_user/', views.new_user, name='new_user'),
]
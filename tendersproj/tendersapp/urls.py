from django.urls import path
from. import views

app_name = 'tendersapp'
urlpatterns = [
    path('index/', views.index, name='index')
]
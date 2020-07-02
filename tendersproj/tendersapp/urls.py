from django.urls import path
from . import views

app_name = 'tendersapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:review_id>/', views.detail, name='detail'),
    path('new_user/', views.new_user, name='new_user'),
    path('new_review/', views.new_review, name='new_review'),
    path('submit_review', views.submit_review, name='submit_review')
]
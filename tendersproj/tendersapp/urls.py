from django.urls import path
from . import views

app_name = 'tendersapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:review_id>/', views.detail, name='detail'),
    path('<int:user_profile_id>/', views.user_profile, name='user_profile'),
    path('new_user/', views.new_user, name='new_user'),
    path('new_review/', views.new_review, name='new_review'),
    path('submit_review', views.submit_review, name='submit_review'),
    path('submit_user', views.submit_user, name='submit_user'),
    path('user_list', views.user_list, name='user_list'),
]
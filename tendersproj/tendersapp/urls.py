from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tendersapp'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:review_id>/', views.detail, name='detail'),
    path('new_review/', views.new_review, name='new_review'),
    path('submit_review', views.submit_review, name='submit_review'),
    path('tendersapp/sign_up/',views.sign_up,name="sign-up"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import TenderReview, Restaurant, User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User


def index(request):
    tenders_review = TenderReview.objects.all()
    context = {
        'tenders_review': tenders_review
    }
    return render(request, 'tendersapp/index.html', context)

def new_user(request): 
    new_user = User()
    context = {
        'new_user': new_user,
    }
    return render(request, 'tendersapp/new_user.html', context)
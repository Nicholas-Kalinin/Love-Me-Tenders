from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import TenderReview, User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import requests


@login_required
def index(request):
    tenders_review = TenderReview.objects.order_by('date_published')
    context = {
        'tenders_review': tenders_review,
    }
    return render(request, 'tendersapp/index.html', context)


def detail(request, review_id):
    tender_review = get_object_or_404(TenderReview, pk=review_id)

    return render(request, 'tendersapp/detail.html',
                  {'tender_review': tender_review})


def new_review(request):
    new_review = TenderReview()
    context = {
        'new_review': new_review,
    }
    return render(request, 'tendersapp/new_review.html', context)


def submit_review(request):
    business_name = request.POST['business_name']
    first_name = request.POST['first_name']
    last_initial = request.POST['last_initial']
    address = request.POST['address']
    city = request.POST['city']
    state = request.POST['state']
    sides = request.POST['sides']
    sauces = request.POST['sauces']
    description = request.POST['description']
    rating = request.POST['rating']
    food_image1 = request.FILES['food_image1']
    food_image2 = request.FILES['food_image2']
    food_image3 = request.FILES['food_image3']
 
    if 'recommend' in request.POST:
        recommend = True
    else:
        recommend = False

    new_rev = TenderReview(business_name=business_name,
                           first_name=first_name,
                           last_initial=last_initial,
                           address=address,
                           city=city,
                           state=state,
                           sides=sides,
                           sauces=sauces,
                           description=description,
                           rating=rating,
                           food_image1=food_image1,
                           food_image2=food_image2,
                           food_image3=food_image3,
                           recommend=recommend)

    new_rev.save()

    return HttpResponseRedirect(reverse('tendersapp:index'))


def upload_image(request):
    food_image1 = request.FILES['food_image1']
    food_image2 = request.FILES['food_image2']
    food_image3 = request.FILES['food_image3']
    upload_image = TenderReview(food_image1=food_image1,
                                food_image2=food_image2,
                                food_image3=food_image3)

    upload_image.save()


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('tendersapp:index'))
    context['form'] = form
    return render(request, 'registration/sign_up.html', context)

def delete_review(request, review_id):
    tender_review = TenderReview.objects.get(id=review_id)
    tender_review = tender_review.delete()
    return HttpResponseRedirect(reverse('tendersapp:index'))
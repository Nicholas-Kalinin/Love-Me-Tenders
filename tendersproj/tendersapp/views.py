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

def detail(request, review_id):  
    tenders_review = get_object_or_404(TenderReview, pk=review_id)  
    return render(request, 'tendersapp/detail.html', {'tenders_review': tenders_review})    

def new_user(request): 
    new_user = User()
    context = {
        'new_user': new_user,
    }
    return render(request, 'tendersapp/new_user.html', context)

def new_review(request): 
    new_review = TenderReview()
    context = {
        'new_review': new_review,
    }
    return render(request, 'tendersapp/new_review.html', context)   

def submit_review(request):
    business_name = request.POST['business_name']
    location = request.POST['location']
    user_name = request.POST['user_name']
    sides = request.POST['sides']
    description = request.POST['description']
    rating = request.POST['rating']
    food_image = request.FILES.get('food_image', None)
    if 'recommend' in request.POST:
        recommend = True
    else:
        recommend = False    


    new_review = TenderReview(business_name=business_name,
                          location=location,
                          user_name=user_name,
                          sides=sides,
                          description=description,
                          rating=rating,
                          food_image=food_image,
                          recommend=recommend,)
    new_review.save()

    return HttpResponseRedirect(reverse('tendersapp:index'))     
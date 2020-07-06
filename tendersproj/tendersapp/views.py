from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import TenderReview, User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
import requests

def index(request):
    tenders_review = TenderReview.objects.order_by('business_name')
    template = loader.get_template('tendersapp/index.html')
    context = {
        'tenders_review': tenders_review,
    }
    return HttpResponse(template.render(context, request))    

def detail(request, review_id):  
    tender_review = get_object_or_404(TenderReview, pk=review_id)  

    return render(request, 'tendersapp/detail.html', {'tender_review':tender_review})    

def new_user(request): 
    new_user = User()
    context = {
        'new_user': new_user,
    }
    return render(request, 'tendersapp/new_user.html', context)

def new_review(request): 
    new_review = TenderReview()
    new_review = User()
    context = {
        'new_review': new_review,
    }
    return render(request, 'tendersapp/new_review.html', context)   

def submit_review(request):
    business_name = request.POST['business_name']
    location = request.POST['location']
    sides = request.POST['sides']
    description = request.POST['description']
    rating = request.POST['rating']
    food_image = request.FILES['food_image']
    if 'recommend' in request.POST:
        recommend = True
    else:
        recommend = False    

                            
  
    new_rev = TenderReview(business_name=business_name,
                              location=location,
                              sides=sides,
                              description=description,
                              rating=rating,
                              food_image=food_image,
                              recommend=recommend)
    
    new_rev.save()

    return HttpResponseRedirect(reverse('tendersapp:index'))

def upload_image(request):
    food_image = request.FILES['food_image']
    upload_image = TenderReview(food_image=food_image)
        
    upload_image.save()
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import TenderReview
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
    tenders_review = TenderReview.objects.order_by('business_name')
    context = {
        'tenders_review': tenders_review,
    }
    return render(request, 'tendersapp/index.html', context)  

def detail(request, review_id):  
    tender_review = get_object_or_404(TenderReview, pk=review_id)  

    return render(request, 'tendersapp/detail.html', {'tender_review':tender_review})    

def new_review(request): 
    new_review = TenderReview()
    context = {
        'new_review': new_review,
    }
    return render(request, 'tendersapp/new_review.html', context)   

def submit_review(request):
    username = request.POST['username']
    date_joined=request.POST['date_joined']
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

                            
  
    new_rev = TenderReview(   username= User.objects.get(id=1), 
                              date_joined=User.objects.get(id=1),    
                              business_name=business_name,
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

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'tendersapp/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context) 

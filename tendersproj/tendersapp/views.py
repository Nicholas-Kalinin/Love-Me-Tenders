from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import TenderReview, User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
import requests
from django.contrib.auth import get_user_model


def index(request):
    tenders_review = TenderReview.objects.all()
    context = {
        'tenders_review': tenders_review
    }
    return render(request, 'tendersapp/index.html', context)

def detail(request, review_id):  
    tender_review = get_object_or_404(TenderReview, pk=review_id)  

    return render(request, 'tendersapp/detail.html', {'tender_review': tender_review}) 

def user_list(request):
    user_profile = User.objects.all()
    context = {
        'user_profile': user_profile
    }
    return render(request, 'tendersapp/user_list.html', context)

def user_profile(request, user_profile_id):  
    user_profile = get_object_or_404(User, pk=user_profile_id)  

    return render(request, 'tendersapp/user_profile.html', {'user_profile': user_profile}) 

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
    food_image = request.FILES.get('food_image', None)
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

    
def submit_user(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    location = request.POST['location']
    profile_image = request.FILES.get('profile_image', None)
    bio = request.POST['bio']

                            
  
    new_user = User(username=User.username,
                    first_name=User.first_name,
                    last_name=User.last_name,
                    email=User.email,
                    location=User.objects.location,
                    profile_image=User.objects.profile_image,
                    bio=User.objects.bio)
        
    new_user.save()

    return HttpResponseRedirect(reverse('tendersapp:users_list')) 
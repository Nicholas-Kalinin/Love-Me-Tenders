from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True) 
    profile_image = models.ImageField(upload_to='profile_image/', null=True, blank=True)

    def __str__(self):
        return self.username

class TenderReview(models.Model):
    location = models.CharField(max_length=50, null=True, blank=True)
    food_image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    sides = models.CharField(max_length=100, null=True, blank=True)
    sauces = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], null=True, blank=True)
    recommend = models.BooleanField(null=True, blank=True)
    business_name = models.CharField(max_length=50)

    def __str__(self):
        return self.location



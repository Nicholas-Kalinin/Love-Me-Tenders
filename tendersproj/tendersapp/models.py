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


class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TenderReview(models.Model):
    location = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.PROTECT, related_name = "user_name")
    food_image = models.ImageField(upload_to='food_image/', null=True, blank=True)
    date_published = models.DateField(auto_now=True)
    sides = models.CharField(max_length=100)
    sauces = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    recommend = models.BooleanField(null=True)
    business = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name = "tenders_review")

    def __str__(self):
        return self.location



from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    username = models.CharField(max_length=30, blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)

class TenderReview(models.Model):
    business_name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=5, null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_initial = models.CharField(max_length=5)
    food_image = models.ImageField(upload_to='images/', null=True, blank=True)
    menu_image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    sides = models.CharField(max_length=100, null=True, blank=True)
    sauces = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], null=True, blank=True)
    recommend = models.BooleanField(null=True, blank=True)    

    def __str__(self):
        return self.business_name



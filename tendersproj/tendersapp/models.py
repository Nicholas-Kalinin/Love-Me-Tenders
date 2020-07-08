from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class TenderReview(models.Model):
    business_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True, blank=True)
    food_image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    sides = models.CharField(max_length=100, null=True, blank=True)
    sauces = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], null=True, blank=True)
    recommend = models.BooleanField(null=True, blank=True)
    username = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user')
    date_joined = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True)

    def __str__(self):
        return self.location



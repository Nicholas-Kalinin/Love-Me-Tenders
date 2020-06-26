from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class TenderReview(models.Model):
    location = models.CharField(max_length=50)
    user_name = models.CharField(max_length=20)
    photo_upload = models.FileField(upload_to='uploads/')
    date_published = models.DateField(auto_now=True)
    sides = models.CharField(max_length=100)
    sauces = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    rating = models.IntegerField()
    recommend = models.BooleanField(null=True)
    business = models.ManyToManyField(Restaurant, related_name='restaurant')

    def __str__(self):
        return self.photo_upload + self.business

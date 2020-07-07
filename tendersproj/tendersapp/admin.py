from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User
from .models import TenderReview

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('bio', 'location','profile_image')}),


admin.site.register(TenderReview)   


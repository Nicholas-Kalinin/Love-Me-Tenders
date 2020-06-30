from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, TenderReview, Restaurant

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('bio', 'location','profile_image')}),

admin.site.register(User, UserAdmin)
admin.site.register(TenderReview)
admin.site.register(Restaurant)

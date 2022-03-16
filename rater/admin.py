from django.contrib import admin
from rater.models import UserProfile,Restaurant,Review
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(UserProfile)


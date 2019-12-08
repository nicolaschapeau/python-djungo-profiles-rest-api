from django.contrib import admin
# import UserProfile model
from profiles_api import models



admin.site.register(models.UserProfile)
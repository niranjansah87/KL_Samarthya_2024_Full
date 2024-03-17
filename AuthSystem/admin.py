from django.contrib import admin
from .models import bool_model,profile_img,Update_Profile
# Register your models here.

admin.site.register(bool_model)
admin.site.register(profile_img)
admin.site.register(Update_Profile)
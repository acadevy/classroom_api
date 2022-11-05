from django.contrib import admin
from .models import CustomUser,UserProfile,Teacher,Student,FileUpload

# Register your models here.
admin.site.register((CustomUser,UserProfile,Teacher,Student,FileUpload))

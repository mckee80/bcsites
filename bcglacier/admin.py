from django.contrib import admin
from .models import Sites, Parks, Ratings, Information, Photo
import cloudinary

cloudinary.config( 
  cloud_name = "bcsites", 
  api_key = "679429527975842", 
  api_secret = "88WIMzIwclcqtiC2fXfrPXmZh3E" 
)

# Register your models here.
admin.site.register(Parks)
admin.site.register(Sites)
admin.site.register(Ratings)
admin.site.register(Information)
admin.site.register(Photo)

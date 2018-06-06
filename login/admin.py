from django.contrib import admin

# Register your models here.
from .models import Userdata,Crawldata

admin.site.register(Userdata)
admin.site.register(Crawldata)

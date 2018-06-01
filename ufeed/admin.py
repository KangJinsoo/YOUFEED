from django.contrib import admin

from .models import Userdata, Crawldata
# Register your models here.

admin.site.register(Userdata)
admin.site.register(Crawldata)
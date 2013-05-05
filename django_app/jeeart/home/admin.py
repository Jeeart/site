#-*- coding:utf-8 -*-
from django.contrib import admin
from home.models import *

class BannerModelAdmin(admin.ModelAdmin):
    list_display = ("is_show","priority","image","last_edit_time")
    ordering = ["-priority","is_show"]
    
class DemolistAdmin(admin.ModelAdmin):
    list_display = ("is_show","priority","image","last_edit_time")
    ordering = ["-priority","is_show"]
    

admin.site.register(BannerModel, BannerModelAdmin)
admin.site.register(Demolist, DemolistAdmin)
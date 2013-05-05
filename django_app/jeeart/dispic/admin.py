#-*- coding:utf-8 -*-
import os
from django.contrib import admin
from dispic.models import DispicEmails

class DispicEmailsAdmin(admin.ModelAdmin):
    list_display = ("email", "submit_time")
    ordering = ["-submit_time"]

admin.site.register(DispicEmails, DispicEmailsAdmin)
#-*- coding:utf-8 -*-
from django.db import models
from django  import forms
# Create your models here.

class DispicEmails(models.Model):
    """Dispic Email"""
    email = models.EmailField(blank=False)
    submit_time = models.DateTimeField(blank=False,null=False,auto_now_add=True) 
    
    def __unicode__(self):
        return  "Email for Dispic [id]:".decode("utf-8") + unicode(self.id)

    class Meta:
        verbose_name_plural = "Emails For Dispic"
        ordering = ['-submit_time']
        
class EmailForm(forms.Form):
    email = forms.EmailField(label="邮箱", error_messages={'required': '邮箱格式错误!'})

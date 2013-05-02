#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class BannerModel(models.Model):
    """Home页焦点图"""
    is_show = models.BooleanField(default=True,help_text="是否显示") 
    priority = models.IntegerField(default=0,help_text="优先级") #优先级
    image = models.ImageField(upload_to="upload/home/banner",help_text="图片 [800x480]")
    title    = models.CharField(max_length=1024,blank=True,help_text="说明文字 [可为空]") 
    link     = models.URLField(max_length=500,help_text="链接 [非空]")
    last_edit_time = models.DateTimeField(auto_now=True) 
    
    def __unicode__(self):
        return  "首页焦点图 id:".decode("utf-8") + unicode(self.id)
        
    class Meta:
        verbose_name_plural = "首页焦点图"
        

class Demolist(models.Model):
    """Home页demo列表"""
    is_show = models.BooleanField(default=True,help_text="是否显示")
    priority = models.IntegerField(default=0,help_text="优先级") #优先级
    image = models.ImageField(upload_to="upload/home/list",help_text="图片 [240x180]")
    title    = models.CharField(max_length=1024,blank=True,help_text="说明文字 [可为空]") 
    link     = models.URLField(max_length=500,help_text="链接 [非空]")
    last_edit_time = models.DateTimeField(auto_now=True) 
    
    def __unicode__(self):
        return  "首页作品列表 id:".decode("utf-8") + unicode(self.id)
        
    class Meta:
        verbose_name_plural = "首页作品列表"
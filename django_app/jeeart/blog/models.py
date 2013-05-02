#-*- coding:utf-8 -*-
import re
from django.db import models
from django  import forms
from django.utils.html import strip_tags

class Category(models.Model):
    """分类"""
    name = models.CharField(max_length=1024,blank=False) 

    def __unicode__(self):
        return  "分类 ".decode("utf-8") + self.name

    class Meta:
        verbose_name_plural = "分类"
        
class Article(models.Model):
    """博客文章"""
    cat = models.ForeignKey(Category,blank=True, null=True, on_delete=models.SET_NULL,verbose_name="分类")
    title  = models.CharField(max_length=1024,blank=False,verbose_name="标题") 
    author_name = models.CharField(max_length=512,null=True,blank=False,db_index=True,verbose_name="贡献者昵称",help_text="对应头像可以通过'站点贡献者'管理") 
    #user_id = models.IntegerField(null=True,blank=True,db_index=True)    
    is_deleted = models.BooleanField(default=False,verbose_name="是否隐藏",help_text="在勾选该选项时，通过/blog/'文章id'/访问也能实现编辑时预览") 
    content = models.TextField(blank=False,verbose_name="文章内容") 
    last_edit_time = models.DateTimeField(auto_now=True) 
    # TODO: add create time

    class Meta:
        verbose_name_plural = "博文"
        ordering = ["-last_edit_time","cat"]


    def __unicode__(self):
        return  "文章 ".decode("utf-8") + self.title
        

    @property
    def content_in_list(self):
        """显示于列表页的内容"""
        content_in_list = self.__class__.content_list_view_split_mark.split(self.content)[0]
        #content_in_list_no_html = strip_tags(content_in_list)
        return content_in_list
        
class Comment(models.Model):
    """评论"""
    article = models.ForeignKey(Article,blank=False, null=False, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(blank=False,null=False,auto_now_add=True) 
    name  = models.CharField(max_length=1024,blank=True) 
    email = models.EmailField(blank=True)
    content = models.TextField(blank=False) 

    def __unicode__(self):
        return  "评论 id:".decode("utf-8") + unicode(self.id)

    class Meta:
        verbose_name_plural = "评论"
        ordering = ['-comment_time']


class CommentForm(forms.Form):
    name = forms.CharField(max_length=100,label="昵称",error_messages={'required': '请告诉我们该怎么称呼您'})
    #email = forms.EmailField(label="邮箱",error_messages={'required': '请告诉我们您的邮箱'})
    email = forms.EmailField(label="邮箱", required=False)
    content = forms.CharField(error_messages={'required': '怎么都说点啥吧,谢谢~'})

class Attachment(models.Model):
    """上传附件"""
    upload_file = models.FileField(upload_to="upload/blog_attachment/%Y/%m",verbose_name="附件",help_text="上传后可在博文中使用该链接")
    comment = models.TextField(blank=True,verbose_name="注释") 
    upload_time = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name_plural = "附件"
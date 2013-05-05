#-*- coding:utf-8 -*-
import os
from django.contrib import admin
from blog.models import Category,Article,Comment,Attachment

class CategoryAdmin(admin.ModelAdmin):
    pass

class ArticleAdmin(admin.ModelAdmin):
    #actions_selection_counter = False //列表界面显示有几个被选中..
    change_form_template = 'blog/admin/change_form.html'
    date_hierarchy = 'last_edit_time'
    list_display = ("title","cat","author_name","last_edit_time")

    ordering = ["-last_edit_time","cat"]

class CommentAdmin(admin.ModelAdmin):
    def content_show(self,obj):
        return obj.content[:24] + "..."
    content_show.short_description = "内容简略"

    list_display = ("article","email","comment_time","content_show")

class AttachmentAdmin(admin.ModelAdmin):
    def upload_file_format(self,obj):
        try:
            return obj.upload_file.name.split(".")[-1]
        except:
            return ""
    upload_file_format.short_description = "格式"


    def upload_file_name(self,obj):
        return os.path.split(obj.upload_file.name)[-1]
    upload_file_name.short_description = "文件名"

    def full_path(self,obj):
        return "<script>document.write(document.location.protocol + '//' + document.location.host)</script>"+ obj.upload_file.url 
    full_path.allow_tags = True

    full_path.short_description = "完整路径"

    def file_size(self,obj):
        return str(obj.upload_file.size/1024) + "KB"
    file_size.short_description  = "文件大小"

    readonly_fields  = ("upload_time",)
    list_display = ("upload_file_name","full_path","file_size","upload_time","comment")        

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Attachment, AttachmentAdmin)

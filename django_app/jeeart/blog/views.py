#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response,get_object_or_404
from django.template import Context, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404, HttpResponse
from blog.models import *


PRE_PAGE_NUM  = 100

def index(request ,cat_id=None,page_num=None):
    cat_list = Category.objects.all()
    blog_list  = Article.objects.filter(is_deleted = False )
    if cat_id:
        blog_list = blog_list.filter(cat_id = cat_id)
    blog_list = blog_list.order_by("-last_edit_time")

    paginator = Paginator(blog_list, PRE_PAGE_NUM) 
    try:
        blog_list = paginator.page(page_num)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)

    if not cat_id:
        cat_id = -1 #为了all时的匹配
    cat_id = int(cat_id)

    return render_to_response("blog/index.html",{"cat_list":cat_list,"cat_id":cat_id,'blog_list':blog_list},context_instance=RequestContext(request))

def index_full(request,cat):
    return index(request,cat_id)
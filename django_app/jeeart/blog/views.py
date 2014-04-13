#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response,get_object_or_404
from django.template import Context, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404, HttpResponse
from blog.models import *


PRE_PAGE_NUM  = 5

def index(request ,cat_id=None,page_num=None):
    cat_list = Category.objects.all()
    blog_list  = Article.objects.filter(is_deleted = False )
    hasPrevPage = False
    hasNextPage = False
    prevPageNum = 0
    nextPageNum = 0

    if cat_id:
        blog_list = blog_list.filter(cat_id = cat_id)
    blog_list = blog_list.order_by("-last_edit_time")

    paginator = Paginator(blog_list, PRE_PAGE_NUM) 

    try:
        blog_list = paginator.page(page_num)
        if int(page_num) > 1:
            hasPrevPage = True
            prevPageNum = int(page_num) - 1
        if int(page_num) < paginator.num_pages:
            hasNextPage = True
            nextPageNum = int(page_num) + 1
    except PageNotAnInteger:
        blog_list = paginator.page(1)
        hasPrevPage = False
        if paginator.num_pages > 1:
            hasNextPage = True
            nextPageNum = 2;
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)
        hasNextPage = False
        if (paginator.num_pages > 1):
            hasPrevPage = True
            prevPageNum = paginator.num_pages - 1
    if not cat_id:
        cat_id = -1 #为了all时的匹配
    cat_id = int(cat_id)

    return render_to_response("blog/index.html",{"cat_list":cat_list,"cat_id":cat_id,'blog_list':blog_list, 'hasPrevPage':hasPrevPage, 'hasNextPage':hasNextPage, 'prevPageNum':prevPageNum, 'nextPageNum':nextPageNum},context_instance=RequestContext(request))

def index_full(request,cat):
    return index(request,cat_id)
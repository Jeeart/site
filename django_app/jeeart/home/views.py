#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response,get_object_or_404
from django.template import Context, RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse

from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from home.models import *

def index_all(request):
    banners = BannerModel.objects.filter(is_show=True).order_by("-priority")[:4]
    demolists = Demolist.objects.filter(is_show=True).order_by("-priority")
    
    grouplists = []
    _pages = len(demolists)/9 + 1
    for i in range(_pages):
        _pagelist = []
        for ii in range(9):
            _index = i*9 + ii
            if _index < len(demolists):
                _item = demolists[_index]
                _pagelist.append(_item)
        grouplists.append(_pagelist)

    page_num = len(grouplists)
        
    return render_to_response("home/index.html",{'banners':banners, 'demolists':demolists, 'grouplists':grouplists, 'page_num':page_num},context_instance=RequestContext(request))


def index_banners(request):
    banners = BannerModel.objects.filter(is_show=True).order_by("-priority")[:4]
    return render_to_response("home/index.html",{'banners':banners},context_instance=RequestContext(request))


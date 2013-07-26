#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response,get_object_or_404
from django.template import Context, RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse

from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.conf import settings

from home.models import *

def index_all(request):
    banners = BannerModel.objects.filter(is_show=True).order_by("-priority")[:4]
    demolists = Demolist.objects.filter(is_show=True).order_by("-priority", "-last_edit_time")
    
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


def json(data):
    encode = settings.DEFAULT_CHARSET
    return HttpResponse(simplejson.dumps(uni_str(data, encode)), mimetype='application/json')

def uni_str(a, encoding):
    if isinstance(a, (list, tuple)):
        s = []
        for i, k in enumerate(a):
            s.append(uni_str(k, encoding))
        return s
    elif isinstance(a, dict):
        s = {}
        for i, k in enumerate(a.items()):
            key, value = k
            s[uni_str(key, encoding)] = uni_str(value, encoding)
        return s
    elif isinstance(a, str) or (hasattr(a, '__str__') and callable(getattr(a, '__str__'))):
        if getattr(a, '__str__'):
            a = str(a)
        return unicode(a, encoding)
    elif isinstance(a, unicode):
        return a
    else:
        return a

@csrf_exempt
def getWorksList(request):
    ret = {"retcode":-1}
    try:
        demolists = Demolist.objects.filter(is_show=True).order_by("-priority", "-last_edit_time")
        data = [];
        s = int(request.GET['s'])
        n = int(request.GET['n'])
        ret['s'] = s
        ret['n'] = n
        ret['total'] = len(demolists)
        
        for i in range(n):
            _index = s + i
            if _index < len(demolists):
                _item = model_to_dict(demolists[_index])
                data.append(_item)

        ret['data'] = data
        ret['retcode'] = 0

        print ret

    except:
        ret['err_message'] = 'SERVER WRONG'

    #return HttpResponse(simplejson.dumps(ret, ensure_ascii = False, encoding="utf-8"), mimetype='application/json')
    return json(ret);


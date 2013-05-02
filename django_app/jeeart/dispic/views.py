#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response,get_object_or_404
from django.template import Context, RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse

from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from dispic.models import *

def index(request):
	return render_to_response("dispic/index.html",{},context_instance=RequestContext(request))
    
def coming(request):
    return render_to_response("dispic/coming.html",{},context_instance=RequestContext(request))
    

@csrf_exempt
def submitEmail(req):
    ret = {"retcode":-1}
    if req.POST:
        try:
            DispicEmails.objects.get(email=req.POST["email"])
            ret["err_msg"] = "email existed"
        except: 
            print 'NO email'
            emailForm = EmailForm(req.POST)
            if emailForm.is_valid():
                dispicEmail = DispicEmails(email = emailForm.cleaned_data["email"])
                dispicEmail.save();
                ret["retcode"] = 0
            else:
                ret["err_msg"] = emailForm.errors
            
    return HttpResponse(simplejson.dumps(ret), mimetype='application/json')

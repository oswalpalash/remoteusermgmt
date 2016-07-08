from django.shortcuts import render,redirect
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.conf import settings
# Create your views here.
import os
from serv.models import Serv
#templ_dir = TEMPLATE_DIRS
def list_all(request):
    all_servs = Serv.objects.all()
    #return HttpResponse()
    return render(request, 'list_serv.html', {'all_servs':all_servs})	 

def add_serv(request): 
    if (request.method=="GET"):
	return render(request, 'add_serv.html')
    if (request.method=="POST"):	
	ipad = request.POST.get("servip")
	r_pass = request.POST.get("passwordinput")
	loc = request.POST.get("textinput")
	Serv_obj = Serv(ip=ipad,rpass=r_pass,location=loc)
	#return HttpResponse(ipad)
	#TODO Add SSH CHECK	
	Serv_obj.save()
	return redirect('/')

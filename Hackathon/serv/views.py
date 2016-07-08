from django.shortcuts import render
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
    

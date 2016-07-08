from django.shortcuts import render,redirect
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.conf import settings
# Create your views here.
import os,paramiko
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
	ssh=paramiko.SSHClient()
	ssh.set_mission_host_key_policy(paramiko.AudoAddPolicy())
	ping_var=os.system('ping -c 1 -W 5 '+ipad)
	if ping_var == 0:
		try:
			ssh.connect(ipad,username='root',password=r_pass)
		except AuthenticationException:
			print "Unauthorized"
		else:
			print "No probs"
	
	else:	
		pass #Server doesn't exsits
	Serv_obj.save()
	return redirect('/')

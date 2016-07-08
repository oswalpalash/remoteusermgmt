from django.shortcuts import render,redirect
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.conf import settings
# Create your views here.
from users.models import Users
from code import listUsers
from serv.models import Serv
def list_users(request,ip):
    a = request.get_full_path().split('/')
    passw = Serv.objects.get(ip=a[2]).rpass
    all_users = listUsers(a[2],passw)
    #return HttpResponse()
    return render(request, 'list_users.html', {'all_servs':all_users,'ip':a[2]})	

def add_user(request):
    if request.method=="GET":
	return render(request, 'add_user.html',{})
    if request.method=="POST":
	upass = request.POST.get("passwordinput")
	userid = request.POST.get("textinput")
	server = request.POST.get("serv")
	projid = request.POST.get("projid")
	servpass = Serv.objects.get(ip=server).rpass
	userz = Users(userid,upass,projid)
	createUser(server,servpass,userid,upass)
	userz.save()
    	return render(request, 'add_user.html',{})

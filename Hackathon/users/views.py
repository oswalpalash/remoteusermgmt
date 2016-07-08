from django.shortcuts import render,redirect
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.conf import settings
# Create your views here.
from users.models import Users
def list_users(request,ip):
    all_users = Users.objects.all()
    #return HttpResponse()
    return render(request, 'list_users.html', {'all_servs':all_users})	

def add_user(request):
    return HttpResponse("works")

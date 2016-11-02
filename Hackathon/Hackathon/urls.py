"""Hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from serv.views import list_all,add_serv,rm_serv
from users.views import list_users,add_user,delete_user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^serv/add$',add_serv),
    url(r'^serv/rm/(?P<ip>\w+)/$',rm_serv),
    url(r'^user/add',add_user),
    url(r'^user/delete',delete_user),
    url(r'^users/(?P<ip>\w+)/?', list_users , name = "ip"),
    url(r'^$',list_all),
]

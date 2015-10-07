from django.shortcuts import render
from .models import SeoUser, Post, Social_VK
from django.views import generic
from .templatetags import filters

def index(request):
    users_id = SeoUser.objects.order_by('id')
    return render(request, 'user/index.html', {'users_id':users_id})
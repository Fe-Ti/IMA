from django.shortcuts import render
#from django.contrib.auth import LoginView
# Create your views here.

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect 
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.urls import reverse

import json

from . import models

def index(request):
    return render(request, 'tegami/index.html')

def profile(request):
    if request.user.is_authenticated:
        chats = models.Chat.objects.filter(users__username=request.user.username).order_by('chat_name')
        return render(request, 'tegami/profile.html', {'chats':chats})
    else:
        return HttpResponseRedirect(reverse('tegami:login'))

def accprofile(request):
    return HttpResponseRedirect(reverse('tegami:profile'))



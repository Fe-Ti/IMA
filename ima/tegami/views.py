from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect 
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User
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

def chat(request, chat_id):
    if request.user.is_authenticated:
        try:
            chat = models.Chat.objects.get(pk=chat_id)
        except models.Chat.DoesNotExist:
            raise Http404("Chat does not exist")

        if chat in models.Chat.objects.filter(users__username=request.user.username):
            msgs = models.User_message.objects.filter(chat=chat_id).order_by('-date')[:100]
            return render(request, 'tegami/chat.html', {'msgs':msgs, 'chat':chat})
        else:
            return HttpResponseRedirect(reverse('tegami:profile'))
    else:
        return HttpResponseRedirect(reverse('tegami:login'))

def send(request, chat_id):
    if request.user.is_authenticated:
        try:
            chat = models.Chat.objects.get(pk=chat_id)
        except models.Chat.DoesNotExist:
            raise Http404("Chat does not exist")

        if chat in models.Chat.objects.filter(users__username=request.user.username):
            if 'message' in request.POST:
                new_msg = chat.user_message_set.create(author=request.user,text=request.POST.dict()['message'])
            return HttpResponseRedirect(reverse('tegami:chat', args=(chat_id,)))
        else:
            return HttpResponseRedirect(reverse('tegami:profile'))
    else:
        return HttpResponseRedirect(reverse('tegami:login'))

def register_form(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('tegami:profile'))
    else:
        return render(request, 'tegami/register_form.html', {'form': AuthenticationForm})

def register(request):
    if not request.user.is_authenticated:
        try:
            uname = request.POST.dict()['username']
            passwd = request.POST.dict()['password']
            new_user = User.objects.create_user(username=uname, password=passwd)
        except:
            return render(request, 'tegami/error_page.html', {'error':"Can't create user!"})
    return HttpResponseRedirect(reverse('tegami:profile'))


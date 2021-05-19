from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Chat(models.Model):
    users = models.ManyToManyField(User)
    chat_name = models.CharField(max_length=100, verbose_name="Chat name")
    
    def __str__(self):
        return self.chat_name


class User_message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=1000, verbose_name="Message text")
    date = models.DateTimeField(auto_now_add=True)
    

    
    def __str__(self):
        return self.text

    

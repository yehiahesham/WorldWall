# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.core.mail import send_mail
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

# from django.template import loader

class index(generic.ListView):
    template_name = 'wall/index.html'
    context_object_name = 'comments'

    def get_queryset(self):
        """Return ALL published questions ."""
        return Message.objects.order_by('-messages_date')

class Profile(generic.DetailView):
        model = User
        template_name = 'wall/profile.html'

def login(request):
    # email=request.POST['email']
    # password=request.POST['pass']
    user = authenticate(email=email, password=password)
    if user is not None:
         # A backend authenticated the credentials
    else:
        # No backend authenticated the credentials

    return HttpResponse("heeey login now ");

def signup(request):
    # name=request.POST['name']
    # email=request.POST['email']
    # password=request.POST['pass']
    # # input vald
    # newUser= User(user_name=name,user_pass=password,user_email=email)
    # newUser.save();
    # send_mail(
    #     'Wellcome '+ name,
    #     'Thank you for joinnig the World Wall !',
    #     'noreply@WorldWall.com',
    #     [email],
    #     fail_silently=False,
    # )
    return HttpResponseRedirect(reverse('wall:index',))

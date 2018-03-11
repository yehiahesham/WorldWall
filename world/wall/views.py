    # Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,render_to_response
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from wall.forms import AuthenticateForm, UserCreateForm
from .models import *

# from django.template import loader

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('wall:login')
    template_name = 'wall/signup.html'

class index(generic.ListView):
    template_name = 'wall/index.html'
    context_object_name = 'comments'

    def get_queryset(self):
        """Return ALL published questions ."""
        return Message.objects.order_by('-messages_date')

class Profile(generic.DetailView):
        model = User
        template_name = 'wall/profile.html'

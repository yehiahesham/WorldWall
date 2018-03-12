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
from django.contrib.auth.decorators import login_required
from wall.forms import SignUpForm
from .models import *

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        #Validating & Extracting Inputs from form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')

            user = authenticate(username=username, password=raw_password, email=email)

            #Sending Email
            send_mail(
                'Wellcome '+username+" !",
                'Thanks For Joinng the Wall .',
                'noreply@WorldWall.com',
                [email],
                fail_silently=False,
            )

            #Login Now
            return HttpResponseRedirect(reverse_lazy('wall:login',))
    else:
        # try again with the form if inputs aren't valid
        form = SignUpForm()
    return render(request, 'wall/signup.html', {'form': form})

class index(generic.ListView):
    template_name = 'wall/index.html'
    context_object_name = 'comments'

    def get_queryset(self):
        """Return ALL published questions Ordered by the date ."""
        return Message.objects.order_by('-messages_date')

def Profile(request,pk):
        """User profiles with their publications and info like email & name"""
        userid=get_object_or_404(User, pk=pk)
        return render(request,'wall/profile.html',
            context={
            'user':userid,
            'comments': list(Message.objects.filter(user_id=pk).order_by('-messages_date'))
            })

@login_required
def publish(request):
        """Method to puclish on wall what user wants to say """
        if(request.POST['message_txt']!=""):
                new_message = Message(user_id =request.user, messages_text=request.POST['message_txt'], messages_date=timezone.now())
                new_message.save()
        return HttpResponseRedirect(reverse('wall:home', ))

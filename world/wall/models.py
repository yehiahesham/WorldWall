# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class User(models.Model):
      # user id is auto generated
      user_name  = models.CharField(max_length=200)
      user_pass  = models.TextField() # Hashed password
      user_email = models.EmailField(max_length=254,unique=True)

      def __str__(self):
          return self.user_name
      # def __str__(self):
      #     return self.user_name

class Message(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    messages_text = models.CharField(max_length=250)
    messages_date = models.DateTimeField('date published')
    def __str__ (self):
        # user = get_object_or_404(User, pk=user_id);
        # u = User.objects.get(id=self.user_id)
        # print(u);
        return self.messages_text
        # return self.messages_text+" ~ "+ User.objects.get(id=self.user_id).__str__() ;

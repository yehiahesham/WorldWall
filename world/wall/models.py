# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    """The Messgae published on the Wall
     I am using another Django default User Along with its authorization & authenticate Methods """

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    messages_text = models.CharField(max_length=250)
    messages_date = models.DateTimeField('date published')
    def __str__ (self):
        return self.messages_text

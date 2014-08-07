from django.db import models
from datetime import date
from django import forms
from django.contrib.auth.models import User,UserManager
from django.utils import timezone
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _

from social_auth.models import UserSocialAuth

from django.core.exceptions import *

# Create your models here.
import requests
import datetime


class City(models.Model):
    name=models.CharField(max_length=100, null=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, default=0, null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, default=0, null=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return unicode(self.name) or u'' 
        




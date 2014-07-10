# Create your views here.
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
#from django.contrib.auth import authenticate, login as auth_login
from social_auth.models import UserSocialAuth
from city.models import *
from charity.models import *
from play.utils import *
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.models import User
import json
from django.contrib.auth import logout as django_logout
from play.forms import *
from django.core.exceptions import *
from datetime import datetime



def test(request):
    try:
        # Retrieve the user account associated with the current subdomain.
        city = City.objects.get(name=request.subdomain)
        return 'ciao'
    except City.DoesNotExist:
        # No user matches the current subdomain, so return a generic 404.
        return '404'
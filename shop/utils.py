# Create your views here.
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
#from django.contrib.auth import authenticate, login as auth_login
from social_auth.models import UserSocialAuth
from play.models import *
from charity.models import *
from shop.models import *
from play.utils import *
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.models import User
import json
from django.contrib.auth import logout as django_logout

from charity.forms import *

from django.core.exceptions import *
from datetime import datetime


def createEvent(request, shop):
	if request.method=='POST':
		title=request.POST.get('title','')
		description=request.POST.get('description','')
		price=request.POST.get('price','')
		coupons_released=request.POST.get('coupons_released','')
		location=request.POST.get('location','')
		Coupon.objects.create(
			title=title,
			description=description,
			price=price,
			shop=shop,
			coupons_released=coupons_released,
			location=location,
			)
		return HttpResponseRedirect('/city/home/')
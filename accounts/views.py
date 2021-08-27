from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
import requests
from django.http import HttpResponse
from django.http import Http404
# from accounts.models import ShortUrls

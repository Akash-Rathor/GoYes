from django import template
from django.contrib.auth.models import User
register = template.Library()
import requests

@register.simple_tag
def getuser_details(id):
    user=User.objects.get(id=id)
    context1 ={
        'username':user.username,
        'first_name':user.first_name,
        'last_name':user.last_name,
        'email':user.last_name,
    }
    return context1
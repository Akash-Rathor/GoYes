from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    redeemHistory,transactionHistory,balance,
    userLocation,pinnedLocation
)

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']

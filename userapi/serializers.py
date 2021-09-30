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


class redeemHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = redeemHistory
        fields = '__all__'


class transactionHistorySerializer(serializers.ModelSerializer):
    Userdata = userSerializer()
    class Meta:
        model = transactionHistory
        fields = ['Userdata','moneyGet','latitute','longitude']


class balanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = balance
        fields = '__all__'
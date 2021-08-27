from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # delete_at = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    class Meta:
        abstract = True

class redeemHistory(TimeStampMixin):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    howMuch = models.IntegerField()

class transactionHistory(TimeStampMixin):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    moneyGet = models.IntegerField()
    latitute = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)

class balance(TimeStampMixin):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    balance = models.IntegerField()


class userLocation(TimeStampMixin):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    address = models.CharField(max_length=500)


class pinnedLocation(TimeStampMixin):
    campaigndays = models.IntegerField()
    latitute = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    TotalMoney = models.IntegerField()
    # endDate = models.DateTimeField(null=True)

    # def save(self):
    #     if self.endDate is None:
    #         self.endDate = self.created_at + datetime.timedelta(self.campaigndays)
    #         pinnedLocation(self).save()

class requestMoneyByUser(TimeStampMixin):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    approved = models.BooleanField(default=False)
    money = models.IntegerField()
    latitute = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    upiId = models.CharField(max_length=100)

    def __repr__(self):
        return self.user_id

class UPIID(TimeStampMixin):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    upiid = models.CharField(max_length=200)

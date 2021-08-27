from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from allauth.socialaccount.models import SocialAccount
from .models import (
    redeemHistory,transactionHistory,balance,
    userLocation,requestMoneyByUser,UPIID
)
# from socialaccount import socialAccount

class UserData(APIView):
    def get(self,request):
        user = SocialAccount.objects.get(user_id=4).extra_data
        # user = SocialAccount.objects.get(user_id=request.user.id).extra_data
        return Response(user)

class redeemHistoryView(APIView):
    def get(self,request):
        data1 = redeemHistory.objects.filter(user_id = request.user.id).values_list('howMuch')
        if len(data1)>1:
            ever_redeemed=True
            redeemed = [i[0] for i in data1]
        else:
            ever_redeemed = False
            redeemed=[]

        data = {
            'ever_redeemed':ever_redeemed,
            'redeemed':redeemed,
        }
        return Response(data)

class transactionHistoryView(APIView):
    def get(self,request):
        data1 = transactionHistory.objects.filter(user_id = request.user.id).values_list('moneyGet','latitute','longitude','created_at')
        if len(data1)>1:
            ever_redeemed=True
            transectionHistory1 = [i[0] for i in data1]
            latitute = [i[1] for i in data1]
            longitute = [i[2] for i in data1]
            Date = [i[3] for i in data1]
        else:
            ever_redeemed = False
            transectionHistory1=[]
            latitute = []
            longitute = []
            Date=[]

        data = {
            'transactionHistory':ever_redeemed,
            'transactions':transectionHistory1,
            'locations': [[latitute[i],longitute[i]] for i in range(len(longitute))],
            'DateTime':Date,
        }
        return Response(data)

class balanceView(APIView):
    def get(self,request):
        balanced = balance.objects.get(user_id = request.user.id)
        if balanced:
            data={
                'Balance':balanced.balance,
            }
        return Response(data)

    def post(self,request):
        if request.user.id==None:#needs to be removed this is just for testing
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            user_id=request.user.id
        if 'added or deducted' in request.data:
            query = balance.objects.get(user_id=user_id)
            if request.data['added or deducted']=='deducted':
                query.balance-=int(request.data['amount'])
                query2 = transactionHistory.objects.create(user_id=request.user.id,moneyGet=-int(request.data['amount']),
                longitude = request.data['longitute'],latitute=request.data['latitute'])
                query.save()
            elif request.data['added or deducted']=='added':
                transactionHistory.objects.create(user_id=request.user.id,moneyGet=int(request.data['amount']),
                longitude = request.data['longitute'],latitute=request.data['latitute'])
                query.balance+=int(request.data['amount'])
                query.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

class userLocationView(APIView):
    def post(self,request):
        try:
            if userLocation.objects.filter(user_id=request.user.id).exists():
                val = userLocation.objects.filter(user_id=request.user.id).update(address=request.data['address'])
                return Response(status=status.HTTP_200_OK)
            else:
                userLocation.objects.create(user_id=request.user.id,address=request.data['address']).save()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class requestMoneyView(APIView):
    def post(self,request):
        if 'money' in request.data:
            if int(request.data['money'])>100:
                upiid = UPIID.objects.get(user_id=request.user.id)
                requestMoneyByUser.objects.create(money=request.data['money'],latitute=request.data['latitute'],
                longitude=request.data['longitute'],user_id=User.objects.get(id=4),upiid=upiid)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#this needs to be connected with admin panel
def onapprove(request,id,money):
    query = balance.objects.get(user_id=id)
    redeemHistory.objects.create(user_id=id,howMuch=money)
    query.balance-=money
    query.save()
    # sendEmail() this needs to be defined to send email to user on successful credit.

class updatePaymentMethodView(APIView):
    def post(self,request):
        if UPIID.objects.filter(user_id=request.user.id).exists():
            UPIID.objects.get(user_id=request.user.id).update(upiid=request.data['upiid'])
        else:
            UPIID.objects.create(user_id=request.user.id,upiid=request.data['upiid'])
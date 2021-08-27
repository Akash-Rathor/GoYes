from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from userapi import views

urlpatterns = [
	path('userdata/', views.UserData.as_view()),
	path('redeemhistory/', views.redeemHistoryView.as_view()),
	path('transactionHistory/', views.transactionHistoryView.as_view()),
	path('balance/', views.balanceView.as_view()),
	path('userLocation/', views.userLocationView.as_view()),
	path('requestmoney/', views.requestMoneyView.as_view()),
	path('updatePaymentMethod/', views.updatePaymentMethodView.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

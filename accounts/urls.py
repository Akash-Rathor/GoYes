
from django.urls import path,include
# from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from accounts import views


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(),name="logout"),
]


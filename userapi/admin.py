from django.contrib import admin
from .models import pinnedLocation,requestMoneyByUser
# Register your models here.
admin.site.register(pinnedLocation)
# admin.site.register(requestMoneyByUser)
from django.contrib import admin
# from .models import State

class requestMoneyByUserAdmin(admin.ModelAdmin):
    list_display = ('user_id','approved','money')
	
    def has_add_permission(self, request):
        return False

admin.site.register(requestMoneyByUser, requestMoneyByUserAdmin)

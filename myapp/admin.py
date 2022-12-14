from django.contrib import admin
from .models import months,user



class userAdmin(admin.ModelAdmin):
    list_display = ('name','contact_no', 'email','age','batch','paid', 'amount','paid_month' , 'date','month')

admin.site.register(months)
admin.site.register(user,userAdmin)
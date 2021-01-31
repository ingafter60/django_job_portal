# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class MyAdminAccounts(UserAdmin):
    model = Account
    list_display 	= ('email','first_name','last_name','is_employee','is_employer')
    list_filter 	= ('email','first_name','last_name','is_employee','is_employer')
    search_fields 	=  ('email','first_name','last_name')
    ordering 		= ('email','first_name')
    readonly_fields = ['date_joined']


# Register your models here.
admin.site.register(Account, MyAdminAccounts)

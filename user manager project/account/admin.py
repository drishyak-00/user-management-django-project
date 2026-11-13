from django.contrib import admin
from .models import CustomeUser

@admin.register(CustomeUser)
class CustomeUserAdmin(admin.ModelAdmin):
    list_display = ['id' , 'email' ,'age' , 'address']
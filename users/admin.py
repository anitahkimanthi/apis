from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Users 

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


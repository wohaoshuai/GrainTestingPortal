from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
from app.models import User_mod, Reports

admin.site.register(User_mod)
admin.site.register(Reports)

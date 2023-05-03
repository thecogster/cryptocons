
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import UserRegisterForm, UserChangeFormCustom
from django.contrib import admin

from .models import *


# class CustomUserAdmin(UserAdmin):
#     add_form = UserRegisterForm
#     form = UserChangeFormCustom
#     model = CustomUser
#     list_display = ['username', 'email']
# admin.site.register(Customer)
# admin.site.register(Product)
# admin.site.register(Tag)

admin.site.register(Business)
admin.site.register(BusinessLoan)
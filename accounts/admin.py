from django.contrib import admin
from .forms import CustomChangeForm, CustomCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    form = CustomChangeForm
    add_form = CustomCreationForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)

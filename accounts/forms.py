from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


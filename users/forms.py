from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import HiddenInput
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
        # , 'firstname', 'lastname', 'phone', 'avatar', 'country'


class UserProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = HiddenInput()
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'country')

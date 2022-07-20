
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import ForEmailForm


class UserForm(UserCreationForm):

    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user



class EmailForm(forms.ModelForm):
    class Meta:
        model = ForEmailForm
        fields = ('email',)


class LoginForm(forms.Form):
    login = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150)



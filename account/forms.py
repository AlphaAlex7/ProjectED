from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":
                    "form-control d-block w-25 mx-auto"
            }
        )
    )

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":
                    "form-control d-block w-25 mx-auto"
            }
        )
    )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('username', 'password')

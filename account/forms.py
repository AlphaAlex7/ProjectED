from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegistrationForms(UserCreationForm):
    username = UsernameField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={
                "class":
                    "form-control d-block w-25 mx-auto"
            }
        )
    )
    email = forms.EmailField(
        label="Почта",
        widget=forms.EmailInput(
            attrs={
                "class":
                    "form-control d-block w-25 mx-auto"
            }
        )
    )
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class":
                    "form-control d-block w-25 mx-auto"
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(
            attrs={
                "class":
                    "form-control d-block w-25 mx-auto"
            }
        ),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = User
        fields = ('username', "email")



class LoginForm(AuthenticationForm):
    username = UsernameField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={
                "class":
                    "form-control d-block w-25 mx-auto"
            }
        )
    )

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
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

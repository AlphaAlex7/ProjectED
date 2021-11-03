from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "class":
                    "p-2 d-block w-25",
                "style":
                    "background:#ffffff; border-radius:0.25rem; border: 1px solid;border-color: #ced4da;"
            }
        ),
        queryset=PostCategory.objects.all(),
        label="Категория")

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":
                    "form-control d-block w-50"
            }
        )
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":
                    "form-control"
            }
        )
    )

    class Meta:
        model = PostModel
        fields = ('title', 'category', 'text')

# 3
# 4
# 5
#
# from django import forms
#
#
# class UserForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={"class": "myfield"}))
#     age = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "myfield"}))

from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=PostCategory.objects.all(), label="Категория")

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
from django import forms
from .models import Categories, News
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label="Title", widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label="Text", required=False,
#                               widget=forms.Textarea(attrs={
#                                   "class": "form-control",
#                                   "rows": 5
#                               }))
#     image = forms.ImageField(label="Picture", required=False)
#     is_publ = forms.BooleanField(label="Published", initial=True)
#     category = forms.ModelChoiceField(queryset=Categories.objects.all(), label="Category",
#                                       widget=forms.Select(attrs={"class": "form-control"}),
#                                       empty_label="-- Choose one --")

class RegForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=30,
                               help_text="Username need to contain only letters, digits and '_'",
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email', max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Enter Password', max_length=50,
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Repeat Password', max_length=50,
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LogForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Enter Password', max_length=50,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "image", "is_publ", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.search('[а-яА-Я]', title):
            raise ValidationError("Title mustn't contain cyrillic letters")
        return title


class MailForm(forms.Form):
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={"class": "form-control"}))
    mes_email = forms.CharField(label='Body', widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    captcha = CaptchaField(label='Captcha')

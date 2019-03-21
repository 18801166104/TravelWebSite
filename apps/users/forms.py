# author wangz
from django import forms
from captcha.fields import CaptchaField


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=8)
    captcha = CaptchaField(error_messages={'invalid': "验证码有误"})


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    username.widget.attrs['class'] = 'text'
    username.widget.attrs['placeholder'] = '登陆邮箱'
    password = forms.CharField(required=True, min_length=8)
    password.widget.attrs['class'] = 'text'
    password.widget.attrs['placeholder'] = '您的密码'

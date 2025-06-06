# -*- codeding = utf-8 -*-
# @Time: 11/09/2021 15:52
# @Author: Changchen
# @File: forms.py
# @Software: PyCharm
from django import forms
#from captcha.fields import CaptchaField
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    #captcha = CaptchaField()

#没做出来
# class ForgetForm(forms.Form):
#      email = forms.EmailField(required=True)
#      captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})

class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'gender', 'birday', 'address', 'mobile']
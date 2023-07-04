from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    email=forms.EmailField(
        max_length=255,
        help_text='이메일 주소를 입력해주세요'
    )
    nickname=forms.CharField(
        max_length=255,
        help_text='닉네임을 입력해주세요'
        required=True
    )
    password1=forms.CharField(
        label='Password'
        widget=forms.PasswordInput(),
        help_text='8문자를 포함하여 비밀번호를 설정해주세요'
    )
    password2=forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(),
        help_text='같은 비밀번호를 적어주세요'
    )
    class Meta:
        model=User
        fields=['email','nickname','password1','password1']
        
class SignInForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['email','password']
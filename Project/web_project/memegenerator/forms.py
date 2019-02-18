from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class RegisterForm(ModelForm):
    #password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=64)
    class Meta:
        model = User
        fields = ['username','password', 'email']
        help_texts = {
            'username': None,
        }
        def save(self):
            user = super(RegistrationForm, self).save()
            user_profile = TeacherProfile(
                username=user,
                email=self.cleaned_data['email']    
            )

            user_profile.save()
            return user, user_profile


class LoginForm(ModelForm):
    # password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=64)
    class Meta:
        model = User
        fields = ['username','password']
        help_texts = {
            'username': None,
        }

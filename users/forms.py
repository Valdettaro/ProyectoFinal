from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            
            Profile.objects.create(user=user)
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_picture',)

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
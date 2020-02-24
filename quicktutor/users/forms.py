from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Homepage, UserProfile

class HomepageForm(ModelForm):
    class Meta:
        model = Homepage
        fields = ['subject']

# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password1',
#             'password2'
#         )

#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']

#         if commit:
#             user.save()

#         return user

class EditProfileForm(UserChangeForm):
    template_name='/something/else'
    password = None

    class Meta:
        model = User
        fields = (
            #'email',
            'first_name',
            'last_name',
            #'password'
        )

class MoreUserInfo(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['year', 'major', 'description']
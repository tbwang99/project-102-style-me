from django import forms
from django.forms import ModelForm
from users.models import Homepage

class HomepageForm(ModelForm):
    class Meta:
        model = Homepage
        fields = ['subject']
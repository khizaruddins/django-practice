from django import forms
from formsApp.models import User
from django.core import validators

def check_for_z(value):
    if value[0] != 'z':
        raise forms.ValidationError("Name must start with letter z")

class MyformsModel(forms.ModelForm):
    name = forms.CharField(validators=[check_for_z])
    class Meta():
        model = User
        fields = '__all__'

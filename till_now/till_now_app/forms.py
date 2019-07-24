from django import forms
from till_now_app.models import User
from django.core import validators

def check_for_z(value):
    if value[0] != 'z':
        raise forms.ValidationError("Name must start from z")

class MyFormModel(forms.ModelForm):
    name = forms.CharField(validators=[check_for_z])

    class Meta():
        model = User
        fields = '__all__'

from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User # model to which it has to be inserted
        fields = '__all__' # for importing all fields

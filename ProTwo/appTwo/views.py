from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
from appTwo.forms import NewUserForm

def index(request):
    return render(request, 'apptwo/index.html')

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            # form.save() will save all form values and commit = True will commit saved form to database
            form.save(commit=True)
            return index(request)
        else:
            print("error form invalid")
    return render(request, 'appTwo/users.html', { 'form': form })

from django.shortcuts import render
from formsApp.models import User
from formsApp.forms import MyformsModel

def index(request):
    form_data = User.objects.all()
    return render(request, 'formsApp/layouts/index.html', { 'form_data':form_data })

def form_view(request):
    form = MyformsModel()
    if request.method == "POST":
        form = MyformsModel(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request, 'formsApp/layouts/form_page.html', { 'form':form } )

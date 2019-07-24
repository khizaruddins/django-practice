from django.shortcuts import render
from till_now_app.models import User, Employee
from till_now_app.forms import MyFormModel

def index(request):
    return render(request, 'till_now_app/index.html')

def form_view(request):
    form = MyFormModel()

    if request.method == "POST":
        form = MyFormModel(request.POST)

        if form.is_valid():
            form.save(commit=True)
            index(request)

    return render(request, 'till_now_app/form_page.html', {'form':form})

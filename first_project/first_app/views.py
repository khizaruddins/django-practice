from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, Webpage, User
from first_app import forms

def index(request):
    web_pages_list = AccessRecord.objects.order_by('date')
    # usr = User.objects.all()
    acc_rec = { 'access_records': web_pages_list }
    return render(request, 'first_app/index.html', context=acc_rec)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        # we pass it that request
        form = forms.FormName(request.POST)

        # check to see form is valid
        if form.is_valid():
            print('form validation success prints in console!!')
            print('Name '+form.cleaned_data['name'])
            print('Email '+form.cleaned_data['email'])
            print('Text '+form.cleaned_data['text'])
    return render(request, 'first_app/form_name.html', {'form': form})

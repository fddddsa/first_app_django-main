from django.shortcuts import render
from django import forms
def index(request):
    userform = UserForm()
    return render(request, "firsatapp/index.html",
            {"form": userform})

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента")
    age = forms.IntegerField(label="Возраст клиента")
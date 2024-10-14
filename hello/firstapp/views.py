from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotModified, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponseGone, HttpResponseServerError
from django.template.response import TemplateResponse

from hello.firstapp.forms import UserForm
#from django.http import *

# Create your views here.
#def index(request):
#    return HttpResponse("Hello World! Это мой первый проект на Django!")

#def index(request):
#    return HttpResponse("<h2>Глaвнaя</h2>")
#def about(request):
#    return HttpResponse("<h2>О сайте</h2>")
#def contact(request):
#    return HttpResponse("<h2>Koнтaкты</h2>")

def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1}</h2>" .format(productid, category)
    return HttpResponse(output)
def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3 >" .format(id, name)
    return HttpResponse(output)

def index(request):
    #return HttpResponse("Index")
    #return render(request, "firstapp/home.html")
    # header = "Персональные данные" # обычная переменная
    # langs = ["Английский", "Немецкий", "Испанский"] # массив
    # user = {"name": "Максим,", "age": 30} # словарь
    # addr = ("Виноградная", 23, 45) # кортеж
    # data = {"header": header, "langs": langs, "user": user, "address":
    # addr}
    # return render(request, "index.html", data)
    
    #data = {"age": 50}
    #return render(request, "firstapp/index.html", context=data)

    #cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"]
    #return render(request, "firstapp/index.html", context={"cat": cat})

    #userform = UserForm()
    #return render(request, "firstapp/index.html", {"form": userform})

    if request.method == "POST":
        name = request.POST.get("name") # получить значения поля Имя
        age = request.POST.get("age") # значения поля Возраст
        output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст – {1}</h3>".format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "firstapp/index.html", {"form": userform})


def about(request):
    #return HttpResponse("About")
    return render(request, "firstapp/about.html")

def contact(request):
    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")




def m304(request):
    return HttpResponseNotModified()
def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")
def m403(request):
    return HttpResponseForbidden ( "<h2>ForЬidden</h2>")
def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")
def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")
def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")
def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")

def index(request):
 return render(request, "firstapp/home.html")

def index(request):
 # return render(request, "firstapp/home.html")
 data = {"header": "Передача параметров в шаблон Django",
 "message": "Загружен шаблон templates/firstapp/index_app1.html"}
 return render(request, "firstapp/index_app1.html", context=data)


def get_data(request):
    header = "Персональные данные" # обычная переменная
    langs = ["Английский", "Немецкий", "Испанский"] # массив
    user = {"name": "Максим", "age": 30} # словарь
    addr = ("Виноградная", 23, 45) # кортеж
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, "index.html", context=data)
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h2>Глaвнaя</h2>")
def about(request):
    return HttpResponse("<h2>0 сайте</h2>")
def contact(request):
    return HttpResponse("<h2>Koнтaкты</h2>")
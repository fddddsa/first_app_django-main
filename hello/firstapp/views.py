from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
def index(request):
 return HttpResponse("Index")
def about(request):
 return HttpResponse("About")
def contact(request):
 return HttpResponseRedirect("/about")
def details(request):
 return HttpResponsePermanentRedirect("/")
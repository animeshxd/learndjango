from django.http import HttpRequest, HttpResponse
# Create your views here.

def index(request: HttpRequest):
    return HttpResponse('<h1> Index </h1>')

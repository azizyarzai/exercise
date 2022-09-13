from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def show_news(request):
    print("request", request.path)
    return HttpResponse("Welcome to Django")

@login_required
def home(request):
    
    #print("request", dir(request))
    #print(request.path)

    # if request.user.is_authenticated:
    return render(request, 'index.html',{"title": "Hello World 2", "name": "Ahmad"})
    # else:
    #     return HttpResponse("Please Login to access this page.")
from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

print('now in views page')

def index(request):
    print('hello world')
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'home.html')
    
from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    # example things to do here:
        # pull data from db,
        # transform data,
        # send email, etc.
    # return HttpResponse("Hello World")
    return render(request, 'hello.html') # returns HttpResponseObject
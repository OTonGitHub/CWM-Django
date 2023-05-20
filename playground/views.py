from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x = 10
    y = 20
    return x * y

def say_hello(request):
    # example things to do here:
        # pull data from db,
        # transform data,
        # send email, etc.
    # return HttpResponse("Hello World")
    # x = 1 # debugging, bp
    # y = 1
    value = calculate() # debug, step into
    return render(request, 'hello.html', {"name": "OT", "value": value}) # returns HttpResponseObject
        # render: HttpRequst, Template, str Dictionary
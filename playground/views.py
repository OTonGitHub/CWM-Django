# reuquest -> response: request handler
# action

from django.shortcuts import render
from django.http import HttpResponse # explicit, handling request (actions)

def calculate():
    x = 10
    y = 20
    return x * y

# Map ->
    # ./urls.py [create_anyName] (., ../startproj [default])
    # import path & .views
    # set urlpatters []
    # path('hello/', view.say_hello) # not function call
    # path('playground/', include('playground.urls')) & import django.url.path, include
    # urlpath: str, pointer to function -> HttpResponseBase Object
    # end route "/" !

def say_hello(request):
    # example things to do here:
        # pull data from db,
        # transform data,
        # send email, etc.
    # return HttpResponse("Hello World")
    # x = 1 # debugging, bp
    # y = 1
    value = calculate() # debug, step into
    # request, template, dictionary (str, any obj [includes, model, string, int array etc])
    return render(request, 'hello.html', {"name": "OT", "value": value}) # returns HttpResponseObject
        # render: HttpRequst, Template, str Dictionary
        # retuns  HttpReponse as promised in path() of urlpatterns
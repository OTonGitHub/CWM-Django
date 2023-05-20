from django.urls import path
from . import views

# URlConf
urlpatterns = [ # spell check, django looks for this variable
    path('hello/', views.say_hello) # reference to function, not calling function
        # always end route with forward slash /
]

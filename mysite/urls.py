from django.urls import path,include
from .views import *
urlpatterns = [

    path('',scrape,name="home"),
    path('delete/',clear,name="delete")
]
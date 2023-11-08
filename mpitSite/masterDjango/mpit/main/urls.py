from django.shortcuts import render
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls)
    path('', include('main.urls'))
]
# Create your views here.

from django.urls import path, include
from . import views

app_name = 'anotherApp'
urlpatterns = [
    path('', views.welcome, name='anotherApp'),    
]


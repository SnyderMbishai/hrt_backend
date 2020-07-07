from django.urls import path

from . import views

app_name = 'vowel'

urlpatterns = [
    path('vowel-service', views.reverse_vowel, name='vowel'),    
]

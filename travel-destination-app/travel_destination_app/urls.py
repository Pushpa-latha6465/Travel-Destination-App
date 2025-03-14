from django.urls import path
from destinations import views

urlpatterns = [
    path('', views.index, name='index'),
]
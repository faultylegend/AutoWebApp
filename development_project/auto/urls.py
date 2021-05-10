from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="auto-home"),
    path('usage/', views.usage, name="auto-usage"),
]
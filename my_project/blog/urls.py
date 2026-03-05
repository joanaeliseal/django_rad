from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('eco/<str:texto>/', views.eco),
    path('info/', views.info),
]
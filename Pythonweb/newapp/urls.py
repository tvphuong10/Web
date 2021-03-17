from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('notify/', views.notify),
    path('login/', views.login),
    path('<int:id>/', views.post),
    path('create/', views.create)
]
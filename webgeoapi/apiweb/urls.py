from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index),
    path('sitio/',views.sitio),
    path('sitio/new/', views.post_sitio)
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('view_picture', views.view_picture, name='view_picture.html')
]

from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.gallery, name='gallery'),
    path('image/<int:pk>/', views.view_image, name='photo'),
    path('add/', views.add_images, name='add'),

]
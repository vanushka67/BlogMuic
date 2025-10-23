from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('photos/', views.photo_list, name='photo_list'),
]
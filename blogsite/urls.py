from django.contrib import admin
from django.urls import path, include
from blogapp import views       #imporing views file from blogapp directory

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('addblog/', views.createBlog, name  = "createBlog"),       #path of url after adding blog
]

from django.contrib import admin
from django.urls import path,include
from otp import views

urlpatterns = [
    path('',views.index,name="home"),
    path('video/<int:id>',views.video,name="video"),
    path('search/',views.search,name="search")
]

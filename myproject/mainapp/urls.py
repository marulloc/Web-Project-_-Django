from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('choice/<int:category_id>',views.choice, name='choice'),
    path('detail',views.detail, name='detail'),
]
from django.contrib import admin
from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:contact_id>/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name='search')
]

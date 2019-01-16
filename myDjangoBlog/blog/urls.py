from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.post_list, name='post_list'),
]

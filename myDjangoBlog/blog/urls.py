from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/', views.post_list, name='post_list'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
]

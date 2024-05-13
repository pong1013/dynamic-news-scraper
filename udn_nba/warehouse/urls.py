from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('content/<int:id>', views.content, name='content'),
]
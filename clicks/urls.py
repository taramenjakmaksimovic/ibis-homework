from django.urls import path

from . import views

urlpatterns = [
    path('<int:campaign>/', views.index, name='index'),
]
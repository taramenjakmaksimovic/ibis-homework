from django.urls import path

from . import views

urlpatterns = [
    path('<int:campaign>/', views.number_of_clicks)
]

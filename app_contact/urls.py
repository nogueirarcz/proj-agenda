from django.urls import path
from app_contact import views

app_name = 'app_contact'

urlpatterns = [
    path('', views.index, name='index'),
]

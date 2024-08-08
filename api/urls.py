from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('banner/', views.banner_list, name='banner'),
]
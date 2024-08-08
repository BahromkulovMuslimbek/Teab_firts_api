from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('banner/', views.banner_list, name='banner'),
    path('product/', views.product_list, name='product'),
    path('faq/', views.faq_list, name='faq'),
    path('testimonial/', views.testimonial_list, name='testimonial'),
]
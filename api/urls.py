from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('banner/list/', views.banner_list, name='banner_list'),
    path('product/list/', views.product_list, name='product_list'),
    path('faq/list/', views.faq_list, name='faq_list'),
    path('testimonial/list/', views.testimonial_list, name='testimonial_list'),

    path('banner/detail/', views.banner_detail, name='banner_detail'),
    path('product/detail/', views.product_detail, name='product_detail'),
    path('faq/detail/', views.faq_detail, name='faq_detail'),
    path('testimonial/detail/', views.testimonial_detail, name='testimonial_detail'),
]
from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('banner/list/', views.banner_list, name='banner_list'),
    path('product/list/', views.product_list, name='product_list'),
    path('faq/list/', views.faq_list, name='faq_list'),
    path('testimonial/list/', views.testimonial_list, name='testimonial_list'),

    path('banner/detail/<int:pk>', views.banner_detail, name='banner_detail'),
    path('product/detail/<int:pk>', views.product_detail, name='product_detail'),
    path('faq/detail/<int:pk>', views.faq_detail, name='faq_detail'),
    path('testimonial/detail/<int:pk>', views.testimonial_detail, name='testimonial_detail'),
]
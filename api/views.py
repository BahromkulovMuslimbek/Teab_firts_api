from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BannerSerializer, ProductSerializer, FaqSerializer, TestimonialSerializer
from main.models import Banner, Product, Faq, Testimonial


@api_view(['GET'])
def banner_list(request):
    banners = Banner.objects.all()
    serializer_data = BannerSerializer(banners, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer_data = ProductSerializer(products, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def faq_list(request):
    banners = Faq.objects.all()
    serializer_data = FaqSerializer(banners, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    serializer_data = TestimonialSerializer(testimonials, many=True)
    return Response(serializer_data.data)

@api_view(['GET'])
def banner_detail(request):
    banners = Banner.objects.all()
    serializer_data = BannerSerializer(banners, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def product_detail(request):
    products = Product.objects.all()
    serializer_data = ProductSerializer(products, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def faq_detail(request):
    banners = Faq.objects.all()
    serializer_data = FaqSerializer(banners, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def testimonial_detail(request):
    testimonials = Testimonial.objects.all()
    serializer_data = TestimonialSerializer(testimonials, many=True)
    return Response(serializer_data.data)
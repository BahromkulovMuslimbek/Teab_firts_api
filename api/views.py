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
def banner_detail(request, pk):
    try:
        banners = Banner.objects.filter(pk=pk)
        if not banners.exists():
            return Response({'error': 'Not found'}, status=404)
        serializer_data = BannerSerializer(banners, many=True)
        return Response(serializer_data.data)
    except Banner.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)


@api_view(['GET'])
def product_detail(request, pk):
    try:
        products = Product.objects.filter(pk=pk)
        if not products.exists():
            return Response({'error': 'Not found'}, status=404)
        serializer_data = ProductSerializer(products, many=True)
        return Response(serializer_data.data)
    except Banner.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)


@api_view(['GET'])
def faq_detail(request, pk):
    try:
        faqs = Faq.objects.filter(pk=pk)
        if not faqs.exists():
            return Response({'error': 'Not found'}, status=404)
        serializer_data = FaqSerializer(faqs, many=True)
        return Response(serializer_data.data)
    except Banner.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)


@api_view(['GET'])
def testimonial_detail(request, pk):
    try:
        testimonials = Testimonial.objects.filter(pk=pk)
        if not testimonials.exists():
            return Response({'error': 'Not found'}, status=404)
        serializer_data = TestimonialSerializer(testimonials, many=True)
        return Response(serializer_data.data)
    except Banner.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BannerSerializer
from main.models import Banner


def banner_list(request):
    banners = Banner.objects.all()
    serializer_data = BannerSerializer(banners, many=BannerSerializer)
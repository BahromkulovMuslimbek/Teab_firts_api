from rest_framework.serializers import ModelSerializer
from main.models import *

class BannerSerializer(ModelSerializer):
    class Meta:
        title = Banner
        fields = '__all__'
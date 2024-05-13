from rest_framework import serializers
from ..models import UdnFocus

class UdnFocusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UdnFocus
        fields = '__all__'

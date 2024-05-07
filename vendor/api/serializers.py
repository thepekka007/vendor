from rest_framework import serializers
from .models import Vendor,PurchaseOrder


class VendorSerializer(serializers.ModelSerializer):
    on_time_delivery_rate = serializers.FloatField()
    quality_rating_avg = serializers.FloatField()
    average_response_time = serializers.FloatField()
    fulfillment_rate = serializers.FloatField()
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

import django_filters

class PurchaseOrderFilter(django_filters.FilterSet):
    # Define the fields you want to filter on
    name = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive containment lookup
    
    class Meta:
        model = PurchaseOrder
        fields = ['vendor']  # Add more fields if needed

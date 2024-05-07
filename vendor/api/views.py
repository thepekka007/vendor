from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import generics,status,filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
# from .models import PurchaseOrder
from .serializers import PurchaseSerializer
from .filters import PurchaseOrderFilter
from rest_framework.views import APIView
from .models import Vendor,PurchaseOrder
from .serializers import VendorSerializer,PurchaseSerializer
from django_filters.rest_framework import DjangoFilterBackend



class CreateAVendors(generics.ListCreateAPIView):
    queryset= Vendor.objects.all()
    serializer_class =  VendorSerializer

# class VendorDetailAPIView(generics.RetrieveAPIView):
#     queryset = Vendor.objects.all()   
#     serializer_class = VendorSerializer


# class VendorUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer 

class VendorRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class CreateAPurchaseOrder(generics.ListCreateAPIView):
#     queryset= PurchaseOrder.objects.all()
#     serializer_class =  PurchaseSerializer

#     def get_queryset(self):
#         return super().get_queryset()
    
class PurchaseOrderList(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PurchaseOrderFilter

# Create your views here.
class PurchaseOrderRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class VendorPerformanceAPIView(APIView):
    serializer_class = VendorSerializer
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
        
        performance_data = {
            "on_time_delivery_rate": vendor.on_time_delivery_rate,
            "quality_rating_avg": vendor.quality_rating_avg,
            "average_response_time": vendor.average_response_time,
            "fulfillment_rate": vendor.fulfillment_rate
        }
        
        return Response(performance_data, status=status.HTTP_200_OK)
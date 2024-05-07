from django.urls import path
from . import views
# from .views import VendorDetailAPIView
from .views import PurchaseOrderList
from .views import VendorPerformanceAPIView
from .views import VendorRetrieveUpdateAPIView,PurchaseOrderRetrieveUpdateAPIView

urlpatterns = [
    path("vendors/", views.CreateAVendors.as_view(), name="Create a vendor"),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor_performance'),
    path("purchase_orders/", views.PurchaseOrderList.as_view(), name="Create a Purchase Order"),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateAPIView.as_view(), name='purchase order details'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateAPIView.as_view(), name='vendor-detail'),
]



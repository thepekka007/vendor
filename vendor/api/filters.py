from django_filters import rest_framework as filters
from .models import PurchaseOrder,Vendor
import django_filters
from .models import PurchaseOrder
# class PurchaseOrderFilter(filters.FilterSet):
#     vendor = filters.ModelChoiceFilter(field_name='vendor', queryset=PurchaseOrder.objects.all())

#     class Meta:
#         model = PurchaseOrder
#         fields = ['vendor']
class PurchaseOrderFilter(django_filters.FilterSet):
    vendor = django_filters.ModelChoiceFilter(field_name='vendor', queryset=Vendor.objects.all())

    class Meta:
        model = PurchaseOrder
        fields = ['vendor']
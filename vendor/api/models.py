from django.db import models
from django.utils import timezone

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    vendor_code = models.CharField(max_length=100)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    
    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def update_performance_metrics(self):
        # Calculate on-time delivery rate
        total_orders = self.purchaseorder_set.count()
        on_time_orders = self.purchaseorder_set.filter(delivery_date__lte=timezone.now()).count()
        self.on_time_delivery_rate = (on_time_orders / total_orders) * 100 if total_orders > 0 else 0

        # Calculate quality rating average
        ratings = self.purchaseorder_set.exclude(quality_rating__isnull=True).values_list('quality_rating', flat=True)
        self.quality_rating_avg = sum(ratings) / len(ratings) if ratings else 0

        # Calculate average response time
        total_response_time = sum((po.acknowledgment_date - po.order_date).total_seconds() for po in self.purchaseorder_set.exclude(acknowledgment_date__isnull=True))
        total_orders_with_response = self.purchaseorder_set.exclude(acknowledgment_date__isnull=True).count()
        self.average_response_time = total_response_time / total_orders_with_response if total_orders_with_response > 0 else 0

        # Calculate fulfillment rate
        total_issues = self.purchaseorder_set.exclude(issue_date__isnull=True).count()
        total_orders = self.purchaseorder_set.count()
        self.fulfillment_rate = ((total_orders - total_issues) / total_orders) * 100 if total_orders > 0 else 0

        self.save()

    def __str__(self):
        return str(self.vendor)


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    class Meta:
        verbose_name_plural = "Historical Performance"

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
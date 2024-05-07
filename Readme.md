Project Title
Vendor Management System

Description
The Vendor Management System is a web-based application designed to streamline the process of managing vendors, purchase orders, and performance metrics. It allows users to create and track purchase orders, monitor vendor performance, and generate reports.

Getting Started
Dependencies

-Django
-Django REST Framework
-Python 3.x

Installing


1.Install dependencies using pip:

            pip install -r requirements.txt

2. Perform migrations:

            python manage.py migrate


Executing program


1.Navigate to the project directory.

2.Run the Django development server:

            python manage.py runserver



Assignment

Vendor Profile Management:

        ● POST /api/vendors/: Create a new vendor
        ● GET /api/vendors/: List all vendors.
        ● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
        ● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
        ● DELETE /api/vendors/{vendor_id}/: Delete a vendor.

Purchase Order Tracking:
        ● POST /api/purchase_orders/: Create a purchase order.
        ● GET /api/purchase_orders/: List all purchase orders with an option to filter by
        vendor.
        ● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
        ● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
        ● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

Vendor Performance Evaluation:

        ● GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance
        metrics.



Help

For any issues or questions, please contact [tintomt01@gmail.com].

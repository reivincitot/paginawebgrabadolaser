from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("orders/", include("orders.urls")),
    path("products/", include("products.urls")),
    path("reports/", include("reports.urls")),
    path("transactions/", include("transaction.urls")),
    path("users/", include("users.urls")),
    path("payments/", include("payments.urls")),
    path("shipping/", include("shipping.urls")),
]

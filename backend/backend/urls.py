from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/orders/", include("orders.urls")),
    path("api/products/", include("products.urls")),
    path("api/reports/", include("reports.urls")),
    path("api/transactions/", include("transactions.urls")),
    path("api/users/", include("users.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/shipping/", include("shipping.urls")),
    path("api/auth/", include('auth.urls')),
]

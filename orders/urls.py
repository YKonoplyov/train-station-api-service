from django.urls import path, include
from rest_framework import routers

from orders.views import OrderViewSet

orders_router = routers.DefaultRouter()
orders_router.register("orders", OrderViewSet)

urlpatterns = [path("", include(orders_router.urls))]

app_name = "orders"

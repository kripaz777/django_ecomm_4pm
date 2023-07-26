from django.urls import path, include
from rest_framework import routers
from .api_views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product_filter', ProductListView.as_view(), name='product_filter'),
    path('product_crud/<int:pk>', ProductDetail.as_view(), name='product_crud'),
]
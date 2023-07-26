from rest_framework import viewsets
from .serializers import *
from .models import *

# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



import django_filters.rest_framework
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import filters
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    search_fields = ['title','description']
    ordering_fields = ['id','name','price']

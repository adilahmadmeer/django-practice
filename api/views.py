from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .assetserializer import asset_serializer
from .models import asset

class assetview(viewsets.ModelViewSet):
    queryset = asset.objects.all()
    serializer_class = asset_serializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    # Field filtering
    filterset_fields = ['mac_address', 'owner', 'status']
    # Keyword search
    search_fields = ['mac_address', 'owner']
    # Ordering fields
    ordering_fields = ['id', 'mac_address']
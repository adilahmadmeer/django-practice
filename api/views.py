from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .assetserializer import asset_serializer
from .models import asset


class assetview(viewsets.ModelViewSet):
    queryset=asset.objects.all()
    serializer_class = asset_serializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Field filtering
    filterset_fields = ['mac', 'ip_address1']

    # Keyword search
    search_fields = ['mac', 'ip_address1']

    # Ordering fields
    ordering_fields = ['id', 'mac']
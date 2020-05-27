from rest_framework import viewsets
from .searilizers import ProductSerializer
from accounts.models import Product


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


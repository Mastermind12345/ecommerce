from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Products

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all().order_by('id')
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]   # Authentication By Token
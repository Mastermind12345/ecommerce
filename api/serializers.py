from rest_framework import serializers
from .models import Products

# serializers to convert model instances to JSON so that the frontend can work with the received data.


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
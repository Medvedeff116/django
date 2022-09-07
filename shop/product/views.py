from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from product.serializers import ProductSerializer

from product.models import Product


# Create your views here.
class ProductAPIView(APIView):
    serializer_class = ProductSerializer

    def get(self, request):

        product = Product.objects.filter(type__name="Phone").values()
        return Response({'products': list(product)}, status=status.HTTP_200_OK)
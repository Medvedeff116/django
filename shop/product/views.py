from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, \
    SAFE_METHODS
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response

from product.serializers import ProductSerializer

from product.models import Product
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class ProductAPIView(APIView):
    serializer_class = ProductSerializer

    def get(self, request):
        product = Product.objects.filter(type__name="Phone").values()
        return Response({'products': list(product)}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({'products': 'ok'}, status=status.HTTP_200_OK)

    def put(self, request):
        return Response({'products': 'ok'}, status=status.HTTP_200_OK)

    def patch(self, request):
        return Response({'products': 'ok'}, status=status.HTTP_200_OK)

    def delete(self, request):
        return Response({'products': 'ok'}, status=status.HTTP_200_OK)


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



    #permission_classes = (IsAdminOrReadOnly, )


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }




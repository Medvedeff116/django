from django.urls import path

from product.views import ProductAPIView

urlpatterns = [
    path('product/', ProductAPIView.as_view()),
]

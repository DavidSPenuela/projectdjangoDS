from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, precio_final

""" urlpatterns = [
    path('products/', Productlist.as_view(), name='product-list'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product-detail'),
] """

router = DefaultRouter()
router.register('products', ProductViewSet, basename = 'products' )
router.register('categories', CategoryViewSet, basename = 'categories')

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>/precio-final/', precio_final),
]
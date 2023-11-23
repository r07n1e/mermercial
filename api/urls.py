from django.urls import include, path
from rest_framework import routers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import obtain_auth_token

from .views import ProductViewSet, CategoryViewSet, UserViewSet, CustomerViewSet, CustomerAddressViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'customer-address', CustomerAddressViewSet,
                basename='customer-address')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('api/', include(router.urls)),
    path(r'api/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth')
]

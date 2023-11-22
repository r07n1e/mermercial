from django.urls import include, path
from rest_framework import routers

from .views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]

from rest_framework import routers

from apps.products.views.v1.brand import BrandViewSet
from apps.products.views.v1.product import ProductViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"brands", BrandViewSet, basename="brands")

urlpatterns = [] + router.urls

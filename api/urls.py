from rest_framework import routers
from .views import ProductViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('product_order', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

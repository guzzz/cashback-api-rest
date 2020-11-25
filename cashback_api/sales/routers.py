from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'sales', views.SaleModelViewSet)
router.register(r'accumulated-cashback-integration', views.AccumulatedFromOutsideApiViewSet)

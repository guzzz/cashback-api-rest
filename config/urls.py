from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework_simplejwt import views as jwt_views

from cashback_api.resellers.routers import router as resellers_router
from cashback_api.sales.routers import router as sales_router

from .schema import schema_view


urlpatterns = [
	re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(resellers_router.urls)),
    path('', include(sales_router.urls)),
]

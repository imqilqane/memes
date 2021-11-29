from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="MEMES API DOCS",
        default_version='v1',
        description="""
        An api that it main role is to store data in a mongoDB database with POST, retrieve it with GET and fo some other actions with PUT , PATCH and DELET
         """,
        terms_of_service="https://www.memes.com/policies/terms/",
        contact=openapi.Contact(email="contact@memes.local"),
        license=openapi.License(name="TEST License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # refresh token request
    path('api-v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # docs
    path('api-v1/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    # my apps
    path('api-v1/memes/', include('memes_app.urls', namespace="memes")),
    path('api-v1/auth/', include('user.urls', namespace='user')),
]

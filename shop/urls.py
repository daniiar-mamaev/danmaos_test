from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Backend for online shop kg",
      default_version='alpha-0.0.1',
      description="This is online shop",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="daniyar.f96@gmail.com"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny, ],
)

swagger_urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('items.urls')),
] + swagger_urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

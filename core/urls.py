from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.todos.views import DeleteAllTodosView

schema_view = get_schema_view(
    openapi.Info(
        title="20-1B API",
        default_version='v1',
        description="Это API, которые были написаны в целях изучения",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tes@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/todos/', include("apps.todos.urls")),
    path('api/v1/users/', include("apps.users.urls")),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/todos/delete_all/', DeleteAllTodosView.as_view(), name='delete_all_todos'),

    # Swagger
    path('swagger/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

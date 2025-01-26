from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
    openapi.Info(
        title="Task App API",
        default_version='v1',
        description="Task management API",
        terms_of_service="https://www.taskmanagementapi.com/policies/terms/",
        contact=openapi.Contact(email="contact@taskmanagementapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('apps.authentication.urls')),
    path('tasks/', include('apps.tasks.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


admin.site.site_header = "Task Admin"
admin.site.site_title = "Task Admin Portal"
admin.site.site_title = "Welcome to the task app administration"
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Django Debug Toolbar
    path("__debug__/", include("debug_toolbar.urls")),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/', include('parking.urls')),
]

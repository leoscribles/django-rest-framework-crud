
from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('admin/', admin.site.urls),
]
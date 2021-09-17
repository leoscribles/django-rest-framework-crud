from django.urls import path
from authentication.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]

# http://127.0.0.1:8000/api/v1/auth/register/
# http://127.0.0.1:8000/api/v1/auth/token/refresh/
# http://127.0.0.1:8000/api/v1/auth/token/

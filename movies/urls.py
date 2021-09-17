from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
]


# http://127.0.0.1:8000/api/v1/movies/
# http://127.0.0.1:8000/api/v1/movies/1/
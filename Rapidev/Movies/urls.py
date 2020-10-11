from django.urls import path
from .  import views
app_name = "Movies"
urlpatterns = [
    path('movies', views.MoviesList.as_view(), name="movielist"),
    path('movie/<int:id>', views.MoviesDetail.as_view(), name="moviedetail")
]
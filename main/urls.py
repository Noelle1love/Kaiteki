from django.urls import path
from main.views import IndexView, BlogView, register_view, AnimeDetailView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('blog/', BlogView.as_view(), name='blogs'),
    path('register/', register_view, name='register'),  # регистрация
    path('anime/<int:pk>/', AnimeDetailView.as_view(), name='anime-details'),
    path('anime/<int:id>/', AnimeDetailView.as_view(), name='anime-details'),

]
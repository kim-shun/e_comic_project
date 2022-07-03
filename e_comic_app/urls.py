from django.urls import path
from . import views

app_name = 'e_comic_app'
urlpatterns = [
    path('', views.EComicIndexView.as_view(), name="e_comic_index"),
    path('comic-create', views.EComicCreateView.as_view(), name="e_comic_create"),
    path('comic-test', views.example, name="e_comic_test"),
]

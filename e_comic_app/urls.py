from django.urls import path
from . import views

app_name = 'e_comic_app'
urlpatterns = [
    path('',views.EComicDisp.as_view(), name="e_comic_disp"),
]
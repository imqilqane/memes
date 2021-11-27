from django.urls import path
from . import views

app_name = "memes_app"

urlpatterns = [
    path('all/', views.ListMyMemesAPIView.as_view(), name="my_memes"),
    path('add/', views.CreateMemeAPIView.as_view(), name="add_meme"),
    path('edit/<str:pk>/', views.UpdateMemeAPIView.as_view(), name="edit_meme"),
    path('delete/<str:pk>/', views.DeleteMemeAPIView.as_view(), name="delete_meme")
]

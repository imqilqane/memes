from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name="register"),
    path('login/', views.LoginAPIView.as_view(), name="login"),
    path('register/verify/', views.VerifyACountAPIView.as_view(), name="verify"),

]

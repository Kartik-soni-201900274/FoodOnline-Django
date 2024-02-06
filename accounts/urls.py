from django.urls import path, include
from . import views


urlpatterns = [
    path("registerUser/", views.registerUser, name="registerUser"),
    path("registerVendor/", views.registerVendor, name="registerVendor"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logout, name="logout"),
]

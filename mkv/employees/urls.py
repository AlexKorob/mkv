from django.urls import path
from . import views

app_name = "employees"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("home/", views.Home.as_view(), name="home"),
    path("registration/", views.Registration.as_view(), name="registration"),
    path("login/", views.LogIn.as_view(), name="login"),
    path("logout/", views.LogOut.as_view(), name="logout"),
    path("thanks-for-registration/", views.ThanksForRegistration.as_view(), name="thanks_for_registration"),
]

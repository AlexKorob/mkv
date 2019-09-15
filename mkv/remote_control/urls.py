from django.urls import path

from . import views

app_name = "remote_control"

urlpatterns = [
    path("send-command/", views.Command.as_view(), name="command"),
]

from django.urls import path
from . import views

app_name = "monitoring"

urlpatterns = [
    path("", views.Monitoring.as_view(), name="monitoring"),
]

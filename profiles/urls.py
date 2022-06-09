from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.signup),
    path("login", views.login),
    path("logout", views.logout_request),
    path("bav", views.become_a_volunteer),
    path("control-panel", views.control_panel),
]

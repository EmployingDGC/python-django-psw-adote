from django.urls import path

from . import views


urlpatterns = [
    path("new/", views.new, name="users_new"),
    path("login/", views.login, name="users_login"),
    path("logout/", views.logout, name="users_logout"),
]

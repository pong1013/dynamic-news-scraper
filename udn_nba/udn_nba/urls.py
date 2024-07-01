# from django.contrib import admin
from django.urls import path, include
from warehouse import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.home),
    path("nba/", include("warehouse.urls")),  # update nba news
    path("nba-restapi/", include("warehouse.restapi.urls")),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("App/", include("App.urls")),
    path('admin/', admin.site.urls)
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.endPoint),
    path("programers/", views.programer_list),
]

from django.urls import path
from .views import SimpleApi

urlpatterns = [path("simple-api/", SimpleApi.as_view(), name="simple-api")]

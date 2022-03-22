from django.urls import path
from .views import *

urlpatterns = [
    path('dinamica/', Dinamica_API.as_view(), name="dinamica"),
]
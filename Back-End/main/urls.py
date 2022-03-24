from django.urls import path
from .views import *

urlpatterns = [
    path('dinamica/', Dinamica_API.as_view()),
    path('dinamica/<int:pk>/', Dinamica_API.as_view()),

    path('vagaDinamica/', Vaga_Dinamica_API.as_view()),
    path('vagaDinamica/<int:pk>/', Vaga_Dinamica_API.as_view()),

    path('avaliacao/', AvaliacaoDinamica_API.as_view()),
]
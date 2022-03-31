from django.urls import path
from .views import *

urlpatterns = [
    path('dinamica/', Dinamica_API.as_view()),
    path('dinamica/<int:pk>/', Dinamica_API.as_view()),

    path('vagaDinamica/', Vaga_Dinamica_API.as_view()),
    path('vagaDinamica/<int:pk>/', Vaga_Dinamica_API.as_view()),

    path('avaliacao/', AvaliacaoDinamica_API.as_view()),

    path('vaga/', Vaga_API.as_view()),
    path('vaga/<int:pk>/', Vaga_API.as_view()),

    path('curso/', Curso_API.as_view()),
    path('curso/<int:pk>/', Curso_API.as_view()),

    path('candidato/', Candidato_API.as_view()),
    path('candidato/<int:pk>/', Candidato_API.as_view()),

    path('respostaDinamica/', Resposta_Dinamica_API.as_view()),
    path('respostaDinamica/<int:pk>/', Resposta_Dinamica_API.as_view()),

    path('aprovacaoDinamica/', AprovacaoDinamica_API.as_view()),
    path('aprovacaoDinamica/<int:pk>/', AprovacaoDinamica_API.as_view()),

    path('entrevista/', Entrevista_API.as_view()),
    path('entrevista/<int:pk>/', Entrevista_API.as_view()),
]
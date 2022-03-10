from django.urls import path
from .views import *

urlpatterns = [
    path('register/', signUp.as_view()),
    path('login/', signIn.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
]
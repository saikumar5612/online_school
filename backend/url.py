from django.urls import path
from .views import home, test, lesson, standard

urlpatterns = [
    path('', home),
    path('test/', test),
    path('lesson/',lesson),
    path('standard/', standard),
]
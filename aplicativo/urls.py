from django.urls import path
from . import views

app_name = 'aplicativo'

urlpatterns = [
    path('', views.lista_pessoas, name='pessoas_lista'),
    path('<int:pk>/', views.detalhes_pessoa, name='detalhes_pessoa')

               ]
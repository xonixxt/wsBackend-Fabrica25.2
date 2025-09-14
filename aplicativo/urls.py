from django.urls import path
from . import views

app_name = 'aplicativo'

urlpatterns = [
    path('', views.lista_pessoas, name='pessoas_lista'),
    path('<int:pk>/', views.detalhes_pessoa, name='detalhes_pessoa'),
    path('excluir/<int:pk>/', views.pessoa_excluir, name='pessoa_excluir'),
    path("editar/<int:pk>", views.pessoa_editar, name="pessoa_editar"),
               ]
from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_carro, name='home'),  # raiz do site
    path('carro_list', listar_carro, name='carro_list'),
    path('cadastrar_carro', cadastrar_carro, name='cadastrar_carro'),
    path('deletar_carro/<int:id>/', deletar_carro, name='deletar_carro'),
    path('editar_carro/<int:id>/', editar_carro, name='editar_carro'),
]

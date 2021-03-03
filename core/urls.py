
from django.urls import path, include
from core.views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_mov_rot,
    lista_mensalista,
    lista_mov_mensalista,
    adicionar_pessoa,
    adicionar_veiculo,
    adicionar_mov_rot,
    add_mensalista,
    adicionar_mov_mensalista,
    update_pessoa,
    update_veiculo,
    update_mov_rot,
    update_mensalista,
    lista_marca,
    update_mov_mensalista,
    delete_pessoa,
    delete_veiculo,
    delete_mov_rot,
    delete_mensalista,
    delete_mov_mensalista,
    core_logout,
    core_register,
)


urlpatterns = [
    path('home', home, name='core_home'),
    # pessoas
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('adicionar_pessoa', adicionar_pessoa, name='core_adicionar_pessoa'),
    path('update_pessoa/<int:id>', update_pessoa, name='core_update_pessoa'),
    path('delete_pessoa/<int:id>', delete_pessoa, name='core_delete_pessoa'),
    # veiculos
    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('adicionar_veiculo', adicionar_veiculo, name='core_adicionar_veiculo'),
    path('update_veiculo/<int:id>', update_veiculo, name='core_update_veiculo'),
    path('delete_veiculo/<int:id>', delete_veiculo, name='core_delete_veiculo'),
    # rotativos
    path('mov_rot', lista_mov_rot, name='core_mov_rot'),
    path('adicionar_mov_rot', adicionar_mov_rot, name='core_add_mov_rot'),
    path('update_mov_rot/<int:id>', update_mov_rot, name='core_update_mov_rot'),
    path('delete_mov_rot/<int:id>', delete_mov_rot, name='core_delete_mov_rot'),
    # mensalistas
    path('mensalista', lista_mensalista, name='core_lista_mensalista'),
    path('adicionar_mensalista', add_mensalista,
         name='core_adicionar_mensalista'),
    path('update_mensalista/<int:id>', update_mensalista,
         name='core_update_mensalista'),

    path('delete_mensalista/<int:id>', delete_mensalista,
         name='core_delete_mensalista'),
    # movimento mensalista
    path('mov_mensalista', lista_mov_mensalista, name='core_mov_mensalista'),
    path('adicionar_mov_mensalista', adicionar_mov_mensalista,
         name='core_adicionar_mov_mensalista'),
    path('update_mov_mensalista/<int:id>', update_mov_mensalista,
         name='core_update_mov_mensalista'),

    path('delete_mov_mensalista/<int:id>', delete_mov_mensalista,
         name='core_delete_mov_mensalista'),
    # marca
    path('marcas', lista_marca, name='core_marca'),

    path('', include('django.contrib.auth.urls')),

    path('logout', core_logout, name='core_logout'),

    path('register', core_register, name='core_register'),
]

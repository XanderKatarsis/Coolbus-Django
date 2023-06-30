from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("preguntas", views.preguntas, name="preguntas"),
    path("productos", views.productos, name="producto"),
    path("servicios", views.servicios, name="servicios"),
    path("registro", views.registro, name="signup"),
    path("crud", views.crud, name="crud"),
    path("userAdd", views.userAdd, name="userAdd"),
    path("userDel/ <str:pk>", views.userDel, name="userDel"),
    path("userEdit/ <str:pk>", views.userEdit, name="userEdit"),
    path("userUpdate", views.userUpdate, name="userUpdate"),
    path("formAdd", views.formAdd, name="formAdd"),
    path("crudTipo", views.crudTipo, name="crudTipo"),
    path("tipoAdd", views.tipoAdd, name="tipoAdd"),
    path("tipoDel/ <str:pk>", views.tipoDel, name="tipoDel"),
    path("tipoEdit/ <str:pk>", views.tipoEdit, name="tipoEdit"),
    path("", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]

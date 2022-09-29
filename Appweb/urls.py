
from django.urls import path
from Appweb.views import *

urlpatterns = [
    path('', mainpage, name = "Inicio"),
    path("vender/",feature1, name = "Vender"),
    path("comprar/",feature2, name = "Comprar"),
    path("cartas/",feature3, name = "Coleccion"),
    path("ingresarCarta/",cartaFormulario, name ="IngresarCarta"),
    path("buscarCarta/",busquedaCarta, name = "BuscarCarta"),
    path("Resultado/",resultados, name= "ResultadoBusqueda"),
    path("ingresarComprador/",compradorFormulario, name = "IngresarComprador"),
    path("ingresarVendedor/",vendedorFormulario, name = "IngresarVendedor"),

]

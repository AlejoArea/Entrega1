from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from Appweb.models import *
from Appweb.forms import *

def mainpage(request):
    return render(request,"Appweb/principal.html")

def feature1(request):

    return render(request,"Appweb/feature1.html")

def feature2(request):

    return render(request,"Appweb/feature2.html")

def feature3(request):

    return render(request,"Appweb/feature3.html")

"""
def cartaFormulario(request):
    if request.method == "POST":
         
        carta = Cartas(nombre=request.POST["carta"], precio=request.POST["precio"] ,stock=request.POST["cantidad"])
        
        carta.save()

        return render(request, "Appweb/principal.html")

    return render(request,"Appweb/IngresarCarta.html")


Alternativo
"""

def cartaFormulario(request):
    if request.method == "POST":
        
        formulario1 = ingresarCarta(request.POST)
        
        if formulario1.is_valid():
            
            info = formulario1.cleaned_data

            carta = Cartas(nombre=info["nombre"], precio=info["precio"],stock=info["stock"])

            carta.save()

        return render(request, "Appweb/principal.html")

    else:

        formulario1 = ingresarCarta()

    return render(request,"Appweb/ingresarCarta.html",{"form1":formulario1})

    
def busquedaCarta(request):

    return render(request,"Appweb/busqueda.html")

def resultados(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        carta = Cartas.objects.filter(nombre__icontains=nombre)

        return render(request,"Appweb/resultados.html", {"carta":carta, "nombre":nombre })
    
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def compradorFormulario(request):
    if request.method == "POST":
        
        formulario2 = ingresarComprador(request.POST)
        
        if formulario2.is_valid():
            
            info = formulario2.cleaned_data

            comprador = Comprador(nombre=info["nombre"], apellido=info["apellido"])

            comprador.save()

        return render(request, "Appweb/principal.html")

    else:

        formulario2 = ingresarComprador()

    return render(request,"Appweb/ingresarComprador.html",{"form2":formulario2})

def vendedorFormulario(request):
    if request.method == "POST":
        
        formulario3 = ingresarVendedor(request.POST)
        
        if formulario3.is_valid():
            
            info = formulario3.cleaned_data

            vendedor = Vendedor(nombre=info["nombre"], apellido=info["apellido"])

            vendedor.save()

        return render(request, "Appweb/principal.html")

    else:

        formulario3 = ingresarVendedor()

    return render(request,"Appweb/ingresarVendedor.html",{"form3":formulario3})
from django import forms

class ingresarCarta(forms.Form):

    nombre = forms.CharField(max_length=60)
    precio = forms.FloatField()
    # imagen
    stock = forms.IntegerField()

class ingresarComprador(forms.Form):

    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)

class ingresarVendedor(forms.Form):

    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
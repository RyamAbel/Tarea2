from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import productos
def Productos(request):
    #return HttpResponse("Nuestra primera vista!")
    misProductos = productos.objects.all().values()
    template = loader.get_template('productos.html')
    context = {
        'misProductos': misProductos,
    }
    return HttpResponse(template.render(context, request))


def BienvenidaProductos(request):
    template = loader.get_template('miTemplate.html')
    return HttpResponse(template.render())
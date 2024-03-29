from django.http import JsonResponse

from .models import Sitio, OrdenServicio 

import json

from django.views.decorators.csrf import csrf_exempt

def index(request):
    context = {
        'status':True,
        'content':'mi prime API-rest con django'
    }
    
    return JsonResponse(context)


def sitio(request):
    listado_sitios = Sitio.objects.all()

    context = {
        'status':True,
        'content':list(listado_sitios.values())
    }

    return JsonResponse(context)
@csrf_exempt
def post_sitio(request):

    json_data = json.loads(request.body)

    nombre = json_data['nombre']
    latitud = json_data['latitud']
    longitud = json_data['longitud']
    direccion = json_data['direccion']
    imagen = json_data['imagen']
   
    nuevo_sitio = Sitio.objects.create(
        nombre=nombre,
        latitud=latitud,
        longitud=longitud,
        direccion=direccion,
        imagen=imagen    
    )  
    dic_nuevo_sitio = {
        'id':nuevo_sitio.id,
        'nombre':nuevo_sitio.nombre,
        'latitud':nuevo_sitio.latitud,
        'longitud':nuevo_sitio.longitud,
        'direccion':nuevo_sitio.direccion,
        'imagen':nuevo_sitio.imagen
    }

    context = {
        'status': True,
        'content':dic_nuevo_sitio
    }
    return JsonResponse(context)

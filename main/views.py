from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import requests
import json
import urllib.request

# Importe el decorador login_required
from django.contrib.auth.decorators import login_required, permission_required

# Restricción de acceso con @login_required
@login_required
@permission_required('main.index_viewer', raise_exception=True)
def index(request):
    
    # Arme el endpoint del REST API
    current_url = request.build_absolute_uri()
    print(current_url)
    
    url = current_url + 'api/v1/landing'
    
    print(url)
    
    contents = urllib.request.urlopen(url).read()
    
    print(contents)
    
    response_dict = json.loads(contents)
    
    print(response_dict)
    
    return HttpResponse("Hello, World!")

def landing(request):
    # return render(request, 'main/base.html')
    
    # Arme el endpoint del REST API
    current_url = request.build_absolute_uri()
    url = current_url + 'api/v1/landing'
    
    # url = 'https://web-production-6ef17.up.railway.app/api/v1/landing/?format=json'
    print(url)
    
    # Petición al REST API
    response_http = requests.get(url)
    response_dict = json.loads(response_http.text)
    
    # print("Endpoint ", url)
    # print("Response ", response_dict)
    
    # Respuestas totales
    total_responses = len(response_dict.keys())
    
    # Valores de la respuesta
    responses = response_dict.values()

    # Objeto con los datos a renderizar
    data = {
        'title': 'Landing - Dashboard',
        'total_responses': total_responses,
        'responses': responses,
        'first_response': list(responses)[0]['saved'],
        'last_response': list(responses)[-1]['saved'],
        'most_response': '04/01/2025'
    }
    
    return render(request, 'main/index.html', data)
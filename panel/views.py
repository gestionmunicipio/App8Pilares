from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (Métodos)
# MVT = Modelo Template Vista -> Acciones (Métodos)
# // Para utilizar el método render, debo agregar mi App (panel) en el settings.py

layout_text = """
    <h1>Sitio web con Django | Gestión Municipal </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a> 
        </li>
        <li>
            <a href="/diagnostico">Diagnóstico de los 8 Pilares</a> 
        </li>                
        <li>
            <a href="/resumen">Resumen del Diagnóstico</a> 
        </li>                        
    </ul>
    <hr/>
"""

def hola_mundo(request):
    return HttpResponse(layout_text + "Hola mundo !!...")

def index(request):
    return render(request, 'index.html')

def index_en(request):
    return render(request, 'index_en.html')

def diagnostico(request):
    return render(request, 'diagnostico.html')

def diagnostico_en(request):
    return render(request, 'diagnostico_en.html')

def personas(request):
    return HttpResponse (f"Proceso creado:")
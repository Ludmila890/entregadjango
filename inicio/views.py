from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

def inicio(request):
    #v1 inicial
    #archivo_abierto = open(r'C:\Users\a\Desktop\modulos_python\entrega django\templates\inicio.html' ,'r')
    #template = Template(archivo_abierto.read())
    #contexto = Context()
    #template_renderizado = template.render(contexto)
    #archivo_abierto.close()
    #return HttpResponse(template_renderizado)
    
    #v2 loader
    #template = loader.get_template('inicio.html')
    
    #dicc = {
    #   'nombre' : 'gaspar',
    #  'apellido' : 'mugre'
        
    #}
    
    
    #template_renderizado = template.render(dicc)
    
    #return HttpResponse(template_renderizado)
    #v3

    dicc = {
        'nombre' : 'gaspar',
        'apellido' : 'mugre'
        
    }
    return render(request, 'inicio.html', dicc)
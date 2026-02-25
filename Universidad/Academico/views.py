from django.shortcuts import redirect, render
from .models import Curso
# Create your views here.
def home (request):
    cursos = Curso.objects.all()
    return render(request, 'gestionCursos.html', {'cursos': cursos})
def registroCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCredito']
    
    curso = Curso.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)
    return redirect('/')
        
def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')

def editarCurso(request, codigo=None):
    if request.method == 'GET':
        # Mostrar el formulario de edición
        curso = Curso.objects.get(codigo=codigo)
        return render(request, 'edicionCurso.html', {'curso': curso})
    elif request.method == 'POST':
        # Guardar los cambios
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        creditos = request.POST['txtCredito']
        
        curso = Curso.objects.get(codigo=codigo)
        curso.nombre = nombre
        curso.creditos = creditos
        curso.save()
        
        return redirect('/')
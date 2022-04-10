from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from HospítalGeneral.models import *
from HospítalGeneral.forms import *

def index(request):
    return HttpResponse("Hello, world. You're at the Hospital General index.")

def doctor(request):
    return render(request,"HospítalGeneral/Doctor.html")

def paciente(request):
    return render(request,"HospítalGeneral/Paciente.html")

def doctorFormulario(request):
      if request.method == 'POST':
            miFormulario = DoctorFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  doctor = Doctor (nombre=informacion['nombre'], apellido=informacion['apellido'],sexo=informacion['sexo'],
                    email=informacion['email'], espacialiad=informacion['especialidad'])
                  doctor.save()
                  return render(request, "Hello, world. You're at the Hospital General index.") 
      else:
            miFormulario= DoctorFormulario() 
      return render(request, "Hello, world. You're at the Hospital General index.", {"miFormulario":miFormulario})

def pacienteFormulario(request):
      if request.method == 'POST':
            miFormulario = PacienteFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  paciente = Paciente (nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'], sexo=informacion['sexo'],
                   email=informacion['email'], fechaDeIngreso=informacion['fechaDeIngreso'])
                  paciente.save()
                  return render(request, "Hello, world. You're at the Hospital General index.") 
      else:
            miFormulario= PacienteFormulario() 
      return render(request, "Hello, world. You're at the Hospital General index.", {"miFormulario":miFormulario})

def buscar(request):
      if  request.GET["dni"]:
            #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }"
            dni = request.GET['dni']
            nombre = Paciente.objects.filter(camada__icontains=dni)
            return render(request, "AppCoder/Paciente.html", {"Nombre":nombre, "DNI:":dni})
      else:
            respuesta = "No enviaste datos"
      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

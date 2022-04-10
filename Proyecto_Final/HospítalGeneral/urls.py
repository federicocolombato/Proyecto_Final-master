from django.urls import path
from HospítalGeneral import views


urlpatterns = [
    path('index', views.index, name ='Index'),
    path('paciente', views.paciente, name ='Paciente'),
    path('doctor', views.doctor, name ='Doctor'),
    path('doctorFormulario', views.doctorFormulario, name="DoctorFormulario"),
    path('pacienteFormulario', views.pacienteFormulario, name="PacienteFormulario"),
]

from django import forms

class DoctorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    sexo = forms.CharField()
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=30)

class PacienteFormulario(forms.Form):   
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    sexo = forms.CharField()
    email = forms.EmailField()
    fechaDeIngreasp = forms.CharField(max_length=30)
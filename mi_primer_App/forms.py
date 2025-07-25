from django import forms
from .models import Curso, Estudiante, Entregable

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'duracion_semanas', 'fecha_inicio', 'activo']

# class CursoForm(forms.Form):
#     nombre = forms.CharField()
#     descripcion = forms.CharField(widget=forms.Textarea, required=False)
#     duracion_semanas = forms.IntegerField(min_value=1, initial=4)
#     fecha_inicio = forms.DateField(
#         widget=forms.DateInput(attrs={'type': 'date'}))
#     activo = forms.BooleanField(required=False, initial=True)


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'edad']

# class EstudianteForm(forms.Form):
#     nombre = forms.CharField(label="Nombre", max_length=100)
#     apellido = forms.CharField(label="Apellido", max_length=100)
#     email = forms.EmailField()
#     edad = forms.IntegerField(min_value=10, max_value=100)
#     fecha_inscripcion = forms.DateField(
#         widget=forms.DateInput(attrs={'type': 'date'}))

class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_entrega', 'entregado', 'estudiante']

# class EntregableForm(forms.Form):
#     nombre = forms.CharField(label="Nombre de la entrega", max_length=100)
#     fecha_entrega = forms.DateField(
#         widget=forms.DateInput(attrs={'type': 'date'}))
#     entregado = forms.BooleanField(required=False, initial=False)
#     estudiante = forms.ModelChoiceField(
#         queryset=None, label="Estudiante")  # Se llenará en la vista

class BuscarCursoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del curso", max_length=100, required=False)
    activo = forms.BooleanField(required=False, initial=True)  # Campo para filtrar por cursos activos
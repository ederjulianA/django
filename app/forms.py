from django import forms
from django.forms import ModelForm
from models import *
from django.contrib.auth.forms import UserCreationForm

class EnlaceForm(ModelForm):
	class Meta:
		model = Enlace
		exclude = ("votos","usuario")


class NuevoUsuario(ModelForm):
	class Meta:
		model = User		

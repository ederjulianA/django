# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template 
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response, render
from models import *
from django.shortcuts import get_object_or_404
from forms import *
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def nuevo_usuario(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = NuevoUsuario()
		template = "nuevoUsuario.html"
	return render_to_response(template, context_instance=RequestContext(request,locals()))			



def hora_actual(request):
	"""
	ahora = datetime.now()
	t = get_template("hora.html")
	c = Context({"hora":ahora,"usuario": "eder"})
	html = t.render(c)
	return HttpResponse(html)
	"""

	now = datetime.now()
	return render_to_response('hora.html',{'hora':now, "Usuario":"Edder"})

@login_required
def add(request):
	categorias =Categoria.objects.all()
	if request.method == "POST":
		form = EnlaceForm(request.POST)
		if form.is_valid():
			enlace = form.save(commit = False)
			enlace.usuario = request.user
			enlace.save()
			return HttpResponseRedirect("/")
	else:
		form = EnlaceForm()
	template = "form.html"
	return render_to_response(template,context_instance = RequestContext(request,locals()))		


def home(request):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.order_by("-votos").all()
	template = "index.html"
	#diccionario = {"categorias":categorias, "enlaces":enlaces}
	return render(request,template,locals())


def categoria(request, id_categoria):
	categorias = Categoria.objects.all()
	cat = get_object_or_404(Categoria,pk=id_categoria)
	#cat = Categoria.objects.get(pk = id_categoria)
	enlaces = Enlace.objects.filter(categoria = cat)
	template = "index.html"
	return render(request,template,locals())

@login_required
def minus(request, id_enlace):
    enlace = Enlace.objects.get(pk=id_enlace)
    enlace.votos = enlace.votos - 1
    enlace.save()
    return HttpResponseRedirect("/")

@login_required
def plus(request, id_enlace):
    enlace = Enlace.objects.get(pk=id_enlace)
    enlace.votos = enlace.votos + 1
    enlace.save()
    return HttpResponseRedirect("/")	


from django.views.generic import ListView, DetailView

class EnlaceListView(ListView):
	model = Enlace
	context_object_name = 'enlaces'
	def get_template_names(self):
		return 'index.html'

class EnlaceDetailView(DetailView):
	model = Enlace
	def get_template_names(self):
		return 'index.html'		


from .serializers import EnlaceSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User

class EnlaceViewSet(viewsets.ModelViewSet):
    queryset = Enlace.objects.all()
    serializer_class = EnlaceSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
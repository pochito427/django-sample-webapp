from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.agenda.forms import AgendaForm
from apps.agenda.models import Contacto

# Create your views here.
def index(request):
	return render(request, 'agenda/index.html')

def agenda_view(request):
	if request.method == 'POST':
		form = AgendaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	else:
		form = AgendaForm()
	return render(request, 'agenda/agenda_form.html', {'form': form})

def agenda_list(request):
	contacto = Contacto.objects.all().order_by('id')
	contexto = {'contactos':contacto}
	return render(request, 'agenda/agenda_list.html', contexto)

def agenda_edit(request, id_contacto):
	contacto = Contacto.objects.get(id=id_contacto)
	if request.method == 'GET':
		form = AgendaForm(instance=contacto)
	else:
		form = AgendaForm(request.POST, instance=contacto)
		if form.is_valid():
			form.save()
		return redirect('contacto_listar')
	return render(request, 'agenda/agenda_form.html', {'form': form})

def agenda_delete(request, id_contacto):
	contacto = Contacto.objects.get(id=id_contacto)
	if request.method == 'POST':
		contacto.delete()
		return redirect('contacto_listar')
	return render(request, 'agenda/agenda_delete.html', {'contacto': contacto})


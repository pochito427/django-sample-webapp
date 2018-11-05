from django import forms

from apps.agenda.models import Contacto

class AgendaForm(forms.ModelForm):

	class Meta:
		model = Contacto

		fields = [
			'nombre',
			'telefono',
			'parentesco',	
		]
		labels = {
			'nombre': 'Nombres y apellidos',
			'telefono': 'Teléfono',
			'parentesco': 'Parentesco',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'parentesco': forms.TextInput(attrs={'class':'form-control'}),
		}
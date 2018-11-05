from django.db import models

# Create your models here.

class Contacto(models.Model):
	nombre = models.CharField(max_length=128)
	telefono = models.CharField(max_length=24)
	parentesco = models.CharField(max_length=64)

	class Meta:
		managed = True
		db_table = 'contactos'
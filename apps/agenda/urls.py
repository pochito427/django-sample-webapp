from django.urls import re_path, path
from apps.agenda.views import index, agenda_view, agenda_list, agenda_edit, agenda_delete

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^nuevo$', agenda_view, name='contacto_crear'),
    re_path(r'^listar$', agenda_list, name='contacto_listar'),
    path('editar/<int:id_contacto>/', agenda_edit, name='contacto_editar'),
    path('borrar/<int:id_contacto>/', agenda_delete, name='contacto_borrar'),
]

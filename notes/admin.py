from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Niveau, Eleve, Enseignant, Matiere

admin.site.register(Niveau)
admin.site.register(Eleve)
admin.site.register(Enseignant)
admin.site.register(Matiere)

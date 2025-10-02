from django.db import models
from .Personne import Personne
from .Niveau import Niveau

class Eleve(Personne):
    identifiant = models.CharField(max_length=20 , default="0000" , unique=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
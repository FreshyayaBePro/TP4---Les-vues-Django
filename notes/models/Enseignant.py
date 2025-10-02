from django.db import models
from .Personne import Personne

class Enseignant(Personne):
    id_enseignant = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
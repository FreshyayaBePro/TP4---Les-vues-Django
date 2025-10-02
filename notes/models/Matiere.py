from django.db import models 
from .Enseignant import Enseignant
from .Niveau import Niveau

        
class Matiere(models.Model) : 
    nom = models.CharField(max_length=50,unique=True) 
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE) 
    niveaux = models.ManyToManyField("Niveau")
    
    def __str__(self):
        return f"{self.enseignant} {self.nom} {self.niveaux}"
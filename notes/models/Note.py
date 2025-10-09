from  django.db import models
from .Eleve import Eleve 
from .Matiere import Matiere 

class Note(models.Model) :
    valeur = models.FloatField(null=True)
    eleve = models.ForeignKey(Eleve , on_delete=models.CASCADE) 
    matiere = models.ForeignKey(Matiere , on_delete=models.CASCADE)
    # related_name (peur être redéfinis dans no models pour une manipulation plus simple dans nos requete usage : e1.note_set.all() / si je le redefini, je fais e1.notes.all() 
def __str__(self):
        return f"{self.valeur} {self.eleve} {self.matiere}"
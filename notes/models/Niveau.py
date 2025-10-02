from  django.db import models 

class Niveau(models.Model) :
    nom = models.CharField( unique=True)
    
    class Meta :
        verbose_name = "Niveau"
        verbose_name_plural = "Niveaux"

    def __str__(self):
        return f"{self.nom}"
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from ..models import Niveau , Eleve , Matiere , Enseignant , Note
from django.db.models import Sum,Avg
def statistiques(request) :
    nb_eleves = Eleve.objects.count() 
    nb_enseignant = Enseignant.objects.count()
    nb_note = Note.objects.count()
    nb_matiere =  Matiere.objects.count()
    
    
    moyenne_generale_par_eleve = []
     
    data = { "nb_eleves" : nb_eleves ,
             "nb_enseignant" : nb_enseignant ,
             "nb_note" : nb_note ,
             "nb_matiere" : nb_matiere ,
             "moyenne_generale_par_eleve" : moyenne_generale_par_eleve,
            }
    
    print(data)
    
    # moyenne générale par élève 
    
   
  
    
    eleves = Eleve.objects.all()
    for e in eleves :
        #moyenne_eleve = e.note_set.all() 
        #notes = Note.objects.aggregate(somme = Sum("valeur"))
        moyenne_eleves = Note.objects.aggregate(moyenne_gen = Avg("valeur"))
        
        moyenne_eleves["eleve"] = e.nom 
        moyenne_generale_par_eleve.append(moyenne_eleves)
        
    moyenne_eleve = Note.objects.annotate(moyenne = Avg("valeur"))
    for i in moyenne_eleve :
         print(i.valeur, i.moyenne)   
        
    return HttpResponse(f'Bienvenue dans les stats : {data}')

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from ..models import Matiere

def matieres(request):
    matieres = Matiere.objects.all() 
    #print(matieres)
    return render(request, "notes/matieres.html", {"matieres": matieres})
    #return HttpResponse(f"Liste des matières : {matieres}")

def matiere(request, id):
    #return HttpResponse(f"Ici, on affichera le détail de la matière avec l'id {id}.")
    matiere = get_object_or_404(Matiere , pk=id)
    return render(request , "notes/matiere.html" ,{"matiere":matiere})

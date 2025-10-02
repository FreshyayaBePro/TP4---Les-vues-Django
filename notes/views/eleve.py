from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from ..models import Eleve

def eleves(request):
        eleves = Eleve.objects.all() 
        return render(request, "notes/eleves.html", {"eleves": eleves})
        #return HttpResponse(f"Liste des élèves : {liste_eleves}")

def eleve(request, id) :
    #return HttpResponse(f"Ici, on affichera le détail de l'élève avec l'id {id}.") 
    eleve = get_object_or_404(Eleve, pk=id)
    return render(request, "notes/eleve.html", {"eleve": eleve})
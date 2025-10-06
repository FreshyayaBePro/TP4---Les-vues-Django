
from django.shortcuts import render,get_object_or_404
from ..models import Niveau

def niveau(request, id):
    #return HttpResponse(f"Ici, on affichera le détail du niveau avec l'id {id}.")
    niveau = get_object_or_404(Niveau, pk=id)
    return render(request , "notes/niveau.html" , {"niveau" : niveau})
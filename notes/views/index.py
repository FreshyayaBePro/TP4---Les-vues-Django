from django.shortcuts import render
# Create your views here.

#from django.http import HttpResponse

def index(request):
    #return HttpResponse("Bonjour tout le monde !")
    #return HttpResponse("Bonbon !")
    return render(request, "notes/index.html")

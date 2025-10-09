import os
import django
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ifnti_l3.settings')
django.setup() 


from notes.models import Eleve, Niveau , Matiere ,Enseignant , Note

Niveau.objects.all().delete()
for i in range(1,4) :
    Niveau.objects.create(
        nom=f"L{i}"
    )

Eleve.objects.all().delete()


niveaux_ = list(Niveau.objects.all())

for i in range(10): 
    Eleve.objects.create(
        identifiant = f"MATRICULE {i}",
        nom = f"BOKOPOLO {i}",
        prenom = f"TAMBA {i}",
        sexe = "M",
        date_naissance = "2005-04-12",
        niveau = random.choice(niveaux_) 
    )
Enseignant.objects.all().delete() 

for i in range (5) :
    Enseignant.objects.create(
        nom = f"Yaya {i}" ,
        prenom = f"bobo {i}",
        sexe = "M",
        date_naissance = "1995-05-17"
    )

Matiere.objects.all().delete()
enseignants = list(Enseignant.objects.all())

for i in range(5):
    matiere = Matiere.objects.create(
        nom = f"Matiere {i}",
        enseignant = random.choice(enseignants)
    )
    # Associer un ou plusieurs niveaux
    matiere.niveaux.set([random.choice(niveaux_)])   # liste obligatoire
    # ou matiere.niveaux.add(random.choice(niveaux_))


eleves = list(Eleve.objects.all())
matieres = list(Matiere.objects.all())
Note.objects.all().delete()

for i in range(10,15) :
    Note.objects.create(
        valeur = f"{i}" ,
        eleve = random.choice(eleves) ,
        matiere = random.choice(matieres) 
    )
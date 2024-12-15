from django.db import models
from users.models import User

class CV(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cv')

class Experience(models.Model):
    poste = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description = models.TextField()
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='experiences')

class Formation(models.Model):
    diplome = models.CharField(max_length=100)
    etablissement = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='formations')

class Langue(models.Model):
    libelle = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='langues')

class Competence(models.Model):
    libelle = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='competences')


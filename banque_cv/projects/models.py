from django.db import models
from cv.models import CV


class Projet(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='projects_projets')


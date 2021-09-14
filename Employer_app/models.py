from django.db import models
from django.utils import timezone

# Create your models here.

class  Département (models.Model):

    nom = models.CharField(max_length=255)

class Meta:
	verbose_name_plural = "départements"

	def __str__(self):
	    return self.nom

class Employee(models.Model):
	prenom = models.CharField(max_length=255)
	nom = models.CharField(max_length=255)
	mail = models.CharField(max_length=255)
	tel = models.CharField(max_length=255)
	salaire = models.CharField(max_length=255)
	date_embauche = models.DateTimeField(default=timezone.now, verbose_name="Date embauche")

class Meta:
	verbose_name_plural = "employés"

	def __str__(self):
	    return self.prenom
	    



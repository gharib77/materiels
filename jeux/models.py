from django.db import models

# Create your models here.
class Personne(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    class Meta:
        db_table='personnes'
    def __str__(self):
        return self.nom
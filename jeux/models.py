from django.db import models

# Create your models here.
class Genre(models.Model):
    libelle=models.CharField(max_length=50)
    class Meta:
        db_table='genres'
    def __str__(self):
        return self.libelle

class Personne(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    date_entr=models.DateField(auto_now=False,auto_now_add=False,null=True)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table='personnes'
    def __str__(self):
        return self.nom
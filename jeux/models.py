from django.db import models

# Create your models here.
class Personne(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    date_entr=models.DateField(auto_now=False,auto_now_add=False,null=True)
    class Meta:
        db_table='personnes'
    def __str__(self):
        return self.nom
from django import forms
from jeux.models import Personne

class FormPers(forms.ModelForm):
    class Meta:
        model=Personne
        fields = '__all__'
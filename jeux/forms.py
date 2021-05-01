from django import forms
from jeux.models import Personne,Genre

class FormPers(forms.ModelForm):
    date_entr = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y')
    )
    class Meta:
        model=Personne
        fields = '__all__'

class FormGenre(forms.ModelForm):
    class Meta:
        model=Genre
        fields = '__all__'
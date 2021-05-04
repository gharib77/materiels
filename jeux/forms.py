from django import forms
from jeux.models import Personne,Genre

class FormPers(forms.ModelForm):
    date_entr = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y')
    )
    date_entr.error_messages['required'] = 'date obligatoire'
    date_entr.error_messages['invalid'] = 'date non valide '
    class Meta:
        model=Personne
        fields = '__all__'

        error_messages = {
            'nom': {
                'required': "nom obligatoire",
            },
            'prenom': {
                'required': "prenom obligatoire",
            },
        }
    def __init__(self, *args, **kwargs):
        super(FormPers, self).__init__(*args, **kwargs)
        self.fields['genre'].empty_label = None

class FormGenre(forms.ModelForm):
    class Meta:
        model=Genre
        fields = '__all__'
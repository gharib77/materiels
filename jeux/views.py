from django.shortcuts import render
from jeux.models import Personne
# Create your views here.
def index(request):
    personnes=Personne.objects.all()
    return render(request,'jeux/index.html',{'personnes':personnes})
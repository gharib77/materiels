from django.shortcuts import render,redirect
from jeux.models import Personne,Genre
from jeux.forms import FormPers,FormGenre
# Create your views here.
def index(request):
    personnes=Personne.objects.all()
    return render(request,'jeux/index.html',{'personnes':personnes})
def add(request):
    form=FormPers(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('jeux:index')
    return render(request,'jeux/add.html',{'form':form})

def addgenre(request):
    form=FormGenre(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('jeux:addgenre')
    return render(request,'jeux/addgenre.html',{'form':form})
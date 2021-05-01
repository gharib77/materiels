from django.shortcuts import render,redirect,get_object_or_404
from jeux.models import Personne,Genre
from jeux.forms import FormPers,FormGenre
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    personnes=Personne.objects.all()
    return render(request,'jeux/index.html',{'personnes':personnes})
def add(request):
    data={}
    form = FormPers(request.POST or None)
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        personnes = Personne.objects.all()
        data['html_Pers_list'] = render_to_string('jeux/listepers.html', {
                'personnes': personnes})
    
    else:
        data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string('jeux/add.html',
        context,
        request=request,
    )
    return JsonResponse(data)
def addgenre(request):
    form=FormGenre(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('jeux:addgenre')
    return render(request,'jeux/addgenre.html',{'form':form})

def edit(request,id):
    personne = get_object_or_404(Personne,id=id)
    form = FormPers(request.POST or None,instance=personne)
    if form.is_valid():
        form.save()
        return redirect('jeux:index')
    context = {'form': form}
    html_form = render_to_string('jeux/edit.html',
        context,
        request=request,
    )
    return JsonResponse({'html_form': html_form})

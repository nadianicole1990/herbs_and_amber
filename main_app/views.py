from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Herb, Tincture

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def supplies(request):
    return render(request, 'supplies.html')

def methods(request):
    return render(request, 'methods.html')

def herbs_index(request):
    herbs = Herb.objects.all()
    return render(request, 'herbs/index.html', { 'herbs': herbs })

def herbs_detail(request, herb_id):
    herb = Herb.objects.get(id=herb_id)
    return render(request, 'herbs/detail.html', { 'herb': herb })

def tinctures_index(request):
    tinctures = Tincture.objects.all()
    return render(request, 'tinctures/index.html', { 'tinctures': tinctures })

def tinctures_detail(request, tincture_id):
    tincture = Tincture.objects.get(id=tincture_id)
    return render(request, 'tinctures/detail.html', { 'tincture': tincture })

class TinctureCreate(CreateView):
    model = Tincture
    fields = '__all__'
    success_url = '/tinctures/'
    
class TinctureUpdate(UpdateView):
    model = Tincture
    fields = ['herbs', 'solvent']
    success_url = '/tinctures/'
    
class TinctureDelete(DeleteView):
    model = Tincture
    success_url = '/tinctures/'
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Herb, Tincture
from .forms import BatchForm

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

class HerbCreate(CreateView):
    model = Herb
    fields = '__all__'
    success_url = '/herbs/'
    
class HerbUpdate(UpdateView):
    model = Herb
    fields = ['material', 'state', 'properties']
    success_url = '/herbs/'
    
class HerbDelete(DeleteView):
    model = Herb
    success_url = '/herbs/'

def tinctures_index(request):
    tinctures = Tincture.objects.all()
    return render(request, 'tinctures/index.html', { 'tinctures': tinctures })

def tinctures_detail(request, tincture_id):
    tincture = Tincture.objects.get(id=tincture_id)
    batch_form = BatchForm()
    return render(request, 'tinctures/detail.html', {
        'tincture': tincture, 'batch_form': batch_form
    })

class TinctureCreate(CreateView):
    model = Tincture
    fields = '__all__'
    success_url = '/tinctures/'
    
class TinctureUpdate(UpdateView):
    model = Tincture
    fields = ['herbs', 'solvent', 'image']
    success_url = '/tinctures/'
    
class TinctureDelete(DeleteView):
    model = Tincture
    success_url = '/tinctures/'
    
def add_batch(request, tincture_id):
    form = BatchForm(request.POST)
    if form.is_valid():
        new_batch = form.save(commit=False)
        new_batch.tincture_id = tincture_id
        new_batch.save()
    return redirect('detail', tincture_id=tincture_id)
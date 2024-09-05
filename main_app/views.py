from django.shortcuts import render
from .models import Tincture

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tinctures_index(request):
    tinctures = Tincture.objects.all()
    return render(request, 'tinctures/index.html', { 'tinctures': tinctures })

def tinctures_detail(request, tincture_id):
    tincture = Tincture.objects.get(id=tincture_id)
    return render(request, 'tinctures/detail.html', { 'tincture': tincture })
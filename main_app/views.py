from django.shortcuts import render

class Tincture():
    def __init__(self, name, herbs, solvent, process):
        self.name = name
        self.herbs = herbs
        self.solvent = solvent
        self.process = process
        
    def __str__(self):
        print(f'{self.name}')

tinctures = [
    Tincture('Calming', 'Chamomile, Lemon Balm, Valerian', 'Vodka', 'TBD'),
    Tincture('Digestion', 'Peppermint, Usnea Lichen, Ginger', 'Vodka', 'TBD'),
    Tincture('Immune Support', 'Ginger, Oregon Grape, Echinacea', 'Vodka', 'TBD'),
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tinctures_index(request):
    return render(request, 'tinctures/index.html', { 'tinctures': tinctures })
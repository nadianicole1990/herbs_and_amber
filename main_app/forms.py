from django.forms import ModelForm
from .models import Herb, Batch

class HerbForm(ModelForm):
  class Meta:
    model = Herb
    fields = ['name', 'material', 'state', 'properties']

class BatchForm(ModelForm):
  class Meta:
    model = Batch
    fields = ['prep_date', 'ready_date']
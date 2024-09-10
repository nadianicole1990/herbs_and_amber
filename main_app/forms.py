from django.forms import ModelForm
from .models import Batch

class BatchForm(ModelForm):
  class Meta:
    model = Batch
    fields = ['prep_date', 'ready_date']

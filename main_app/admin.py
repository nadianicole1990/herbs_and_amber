from django.contrib import admin
from .models import Herb, Tincture, Batch

# Register your models here.
admin.site.register(Herb)
admin.site.register(Tincture)
admin.site.register(Batch)
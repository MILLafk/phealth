from django.contrib import admin

# Register your models here.
from .models import Admission, Crud
from .forms import AdmisForm

class AdmissionAdmin(admin.ModelAdmin):
    form = AdmisForm
    class Media:
        js = ('js/custom_admin.js',)

admin.site.register(Admission, AdmissionAdmin)
admin.site.register(Crud)
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Crud, Hosp, Admission
from .forms import CrudForm, HospForm, AdmisForm
from django.db.models import Q

# Create your views here.
def crud_list(request):
    query = request.GET.get('q')
    cruds = Crud.objects.all()
    hosps = Hosp.objects.all()

    if query:
        cruds = cruds.filter(
            Q(phealth_no__icontains=query) |
            Q(lastName__icontains=query) |
            Q(firstName__icontains=query) |
            Q(middleName__icontains=query)
            # Add more fields as needed for search
        )

    return render(request, 'html/crud_list.html', {'cruds': cruds, 'hosps': hosps, 'query': query})

def admission_list(request, phealth_no):
    admissions = Admission.objects.filter(phNo=phealth_no)
    return render(request, 'html/admission_list.html', {'admissions': admissions})

def crud_detail(request, pk):
    crud = get_object_or_404(Crud, pk=pk)
    return render(request, 'html/crud_detail.html', {'crud': crud})

def crud_create(request):
    if request.method == "POST":
        form = CrudForm(request.POST)
        if form.is_valid():
            crud = form.save()
            return redirect('crud_detail', pk=crud.pk)
    else:
        form = CrudForm()
    return render(request, 'html/crud_form.html', {'form': form})

def crud_update(request, pk):
    crud = get_object_or_404(Crud, pk=pk)
    if request.method == "POST":
        form = CrudForm(request.POST, instance=crud)
        if form.is_valid():
            crud = form.save()
            return redirect('crud_detail', pk=crud.pk)
    else:
        form = CrudForm(instance=crud)
    return render(request, 'html/crud_form.html', {'form': form})

def crud_delete(request, pk):
    crud = get_object_or_404(Crud, pk=pk)
    if request.method == "POST":
        crud.delete()
        return redirect('crud_list')
    return render(request, 'html/crud_confirm_delete.html', {'crud': crud})
#################################################################################
def hosp_detail(request, pk):
    hosp = get_object_or_404(Hosp, hospital_id=pk)
    return render(request, 'html/hosp_detail.html', {'hosp': hosp})

def hosp_create(request):
    if request.method == "POST":
        form = HospForm(request.POST)
        if form.is_valid():
            hosp = form.save()
            return redirect('hosp_detail', pk=hosp.pk)
    else:
        form = HospForm()
    return render(request, 'html/hosp_form.html', {'form': form})

def hosp_update(request, pk):
    hosp = get_object_or_404(Hosp, pk=pk)
    if request.method == "POST":
        form = HospForm(request.POST, instance=hosp)
        if form.is_valid():
            hosp = form.save()
            return redirect('hosp_detail', pk=hosp.pk)
    else:
        form = HospForm(instance=hosp)
    return render(request, 'html/hosp_form.html', {'form': form})

def hosp_delete(request, pk):
    hosp = get_object_or_404(Hosp, pk=pk)
    if request.method == "POST":
        hosp.delete()
        return redirect('crud_list')
    return render(request, 'html/hosp_confirm_delete.html', {'hosp': hosp})
#################################################################################
def admis_list(request):
    admis = Admission.objects.all()
    return render(request, 'html/admis_list.html', {'admis': admis})

def admis_detail(request, pk):
    admi = get_object_or_404(Admission, pk=pk)
    return render(request, 'html/admis_detail.html', {'admi': admi})

def admis_create(request):
    if request.method == "POST":
        form = AdmisForm(request.POST)
        if form.is_valid():
            admi = form.save()
            return redirect('admis_detail', pk=admi.pk)
    else:
        form = AdmisForm()

    cruds = Crud.objects.all()
    hosps = Hosp.objects.all()
    
    return render(request, 'html/admis_form.html', {'form': form, 'cruds': cruds, 'hosps': hosps})

def admis_update(request, pk):
    admi = get_object_or_404(Admission, pk=pk)
    if request.method == "POST":
        form = AdmisForm(request.POST, instance=admi)
        if form.is_valid():
            admi = form.save()
            return redirect('admis_detail', pk=admi.pk)
    else:
        form = AdmisForm(instance=admi)
    
    cruds = Crud.objects.all()
    hosps = Hosp.objects.all()
    
    return render(request, 'html/admis_form.html', {'form': form, 'cruds': cruds, 'hosps': hosps})

def admis_delete(request, pk):
    admi = get_object_or_404(Admission, pk=pk)
    if request.method == "POST":
        admi.delete()
        return redirect('admis_list')
    return render(request, 'html/admis_confirm_delete.html', {'admi': admi})
################################################################################
def get_crud_form(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        phealth_no = request.GET.get('phealth_no', None)
        if phealth_no:
            try:
                crud_instance = Crud.objects.get(phealth_no=phealth_no)
                form = CrudForm(instance=crud_instance)
                form_html = render(request, 'html/crud_form.html', {'form': form}).content.decode('utf-8')
                return JsonResponse({'form_html': form_html})
            except Crud.DoesNotExist:
                pass  # Handle case where Crud instance with given phealth_no doesn't exist
    return JsonResponse({'form_html': ''})
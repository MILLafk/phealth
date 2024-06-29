from django import forms
from .models import Crud, Hosp, Admission

class DateInput(forms.DateInput):
    input_type = 'date'

class CrudForm(forms.ModelForm):
    class Meta:
        model = Crud
        fields = ['phealth_no', 'lastName', 'firstName', 'middleName', 'published_date']
        labels = {
            'phealth_no': 'PhilHealth Number',
            'lastName': 'Last Name',
            'firstName': 'First Name',
            'middleName': 'Middle Name',
            'published_date': 'Date',
        }
        widgets = {
            'published_date': DateInput(),
        }  

class HospForm(forms.ModelForm):
    class Meta:
        model = Hosp
        fields = ['hospital_id', 'hospitalName', 'hospitalAddr', 'otherInfo', 'email', 'mobileNo']
        labels = {
            'hospital_id': 'Hospital ID',
            'hospitalName': 'Hospital Name',
            'hospitalAddr': 'Hospital Address',
            'otherInfo': 'Other Information',
            'email': 'Email',
            'mobileNo': 'Mobile Number',
        }

class AdmisForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['admID', 'phNo', 'hosp_id', 'admDate', 'discDate', 'diag', 'rmrks']
        exclude = ['admID']
        labels = {
            'admID': 'Admission ID',
            'phNo': 'PhilHealth Number',
            'hosp_id': "Hospital ID", 
            'admDate': 'Admission Date', 
            'discDate': 'Discharge Date', 
            'diag': 'Diagnosis', 
            'rmrks': 'Remarks',
        }
        widgets = {
            'admDate': DateInput(),
            'discDate': DateInput(),
        }        
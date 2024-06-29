from django.db import models
import uuid

# Create your models here.
class Crud(models.Model):
    phealth_no = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=200)
    published_date = models.DateField()

    def __str__(self):
        return self.title

class Hosp(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    hospitalName = models.CharField(max_length=200)
    hospitalAddr = models.CharField(max_length=200)
    otherInfo = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobileNo = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Admission(models.Model):
    admID = models.CharField(max_length=200, unique=True, editable=False, default=uuid.uuid4)
    phNo = models.CharField(max_length=200)
    hosp_id = models.CharField(max_length=200)
    admDate = models.DateField()
    discDate = models.DateField()
    diag = models.CharField(max_length=200)
    rmrks = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
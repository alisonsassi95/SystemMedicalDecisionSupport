from django.db import models
from patient.models import DataPatient

class ValidationPatient(models.Model):
    idPatient = models.ForeignKey(DataPatient, on_delete=models.PROTECT)
    validationNumber = models.IntegerField()
    medicalName = models.CharField(max_length=200)
    medicalClassification = models.IntegerField()
    class Meta:
        db_table = 'validation_patient'

    def __str__(self):
        return self.medicalClassification
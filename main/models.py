from django.db import models

class Patient(models.Model):
	name = models.CharField(max_length=100, blank=False)
	Pid =  models.CharField(max_length = 9, unique = True, blank=False)
	address = models.CharField(max_length = 300, blank=True, null=True)
	birthday = models.DateField(blank=True, null=True)
	phone = models.CharField(max_length=10, blank=True, default=000)
	mobile = models.CharField(max_length=10, blank=True, default=000)
	photo = models.ImageField(blank=True, null=True)
	sickDate = models.DateField(blank=True, null=True)
	recoveryDate = models.DateField(blank=True, null=True)

	

class Vaccine(models.Model):
	# patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	patient_id = models.CharField(max_length=10, default=0)
	vacDate = models.DateField(blank=False)
	producer = models.CharField(max_length=100, blank=False)






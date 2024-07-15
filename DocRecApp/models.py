from django.db import models

# Create your models here.


# superuser
# username = admin
# password = 123

class Location(models.Model):
  name = models.CharField(max_length=255)
  latitude = models.FloatField()
  longitude = models.FloatField()

  def __str__(self):
    return self.name


class Doctor(models.Model):
  name = models.CharField(max_length=255)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  visit_count = models.IntegerField(default=0)
  def __str__(self):
    return self.name

class Patient(models.Model):
  name = models.CharField(max_length=255)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  


class Visit(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  visit_date = models.DateTimeField(auto_now_add= True)


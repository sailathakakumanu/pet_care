from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pet_photos/')

class MedicalRecord(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    type_of_record = models.CharField(max_length=100)
    date = models.DateField()
    notes = models.TextField()

class EmergencyContact(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    contact_type = models.CharField(max_length=50)

class CarePlan(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    routine = models.TextField()
    feeding_schedule = models.TextField()
    exercise_plan = models.TextField()
    special_instructions = models.TextField()

from django import forms
from .models import Pet, MedicalRecord, EmergencyContact, CarePlan

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'breed', 'photo']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['type_of_record', 'date', 'notes']

class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['name', 'phone_number', 'email', 'contact_type']

class CarePlanForm(forms.ModelForm):
    class Meta:
        model = CarePlan
        fields = ['routine', 'feeding_schedule', 'exercise_plan', 'special_instructions']

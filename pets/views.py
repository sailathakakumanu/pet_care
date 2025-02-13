from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Pet, MedicalRecord, EmergencyContact, CarePlan
from .forms import PetForm, MedicalRecordForm, EmergencyContactForm, CarePlanForm


def add_emergency_contact(request, id):
    return render(request, 'pets/add_emergency_contact.html')

# List of Pets
def pet_list(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'pet_list.html', {'pets': pets})

# Pet Detail Page
def pet_detail(request, id):
    pet = get_object_or_404(Pet, id=id, user=request.user)
    return render(request, 'pet_detail.html', {'pet': pet})

# Create Pet Profile
def create_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            messages.success(request, "Pet created!")
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'create_pet.html', {'form': form})

# Update Pet Profile
def update_pet(request, id):
    pet = get_object_or_404(Pet, id=id, user=request.user)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, "Pet updated!")
            return redirect('pet_detail', id=pet.id)
    else:
        form = PetForm(instance=pet)
    return render(request, 'update_pet.html', {'form': form})

# Delete Pet Profile
def delete_pet(request, id):
    pet = get_object_or_404(Pet, id=id, user=request.user)
    pet.delete()
    messages.success(request, "Pet deleted!")
    return redirect('pet_list')

# Add Medical Record
def add_medical_record(request, id):
    pet = get_object_or_404(Pet, id=id, user=request.user)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.pet = pet
            record.save()
            messages.success(request, "Medical record added!")
            return redirect('view_medical_records', id=pet.id)
    else:
        form = MedicalRecordForm()
    return render(request, 'add_medical_record.html', {'form': form})

# View Medical Records
def view_medical_records(request, id):
    pet = get_object_or_404(Pet, id=id, user=request.user)
    records = MedicalRecord.objects.filter(pet=pet)
    return render(request, 'view_medical_records.html', {'pet': pet, 'records': records})

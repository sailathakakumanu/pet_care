from django.urls import path
from pets import views

from pets.views import view_emergency_contacts

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('create/', views.create_pet, name='create_pet'),
    path('pet/<int:id>/', views.pet_detail, name='pet_detail'),
    path('pet/<int:id>/update/', views.update_pet, name='update_pet'),
    path('pet/<int:id>/delete/', views.delete_pet, name='delete_pet'),

    # For adding and viewing medical records
    path('pet/<int:id>/add_medical_record/', views.add_medical_record, name='add_medical_record'),
    path('pet/<int:id>/medical_records/', views.view_medical_records, name='view_medical_records'),

    # For adding and viewing emergency contacts
    path('pet/<int:id>/add_emergency_contact/', views.add_emergency_contact, name='add_emergency_contact'),
    path('pet/<int:id>/emergency_contacts/', views.view_emergency_contacts, name='view_emergency_contacts'),

    # For creating and viewing care plans
    path('pet/<int:id>/create_care_plan/', views.create_care_plan, name='create_care_plan'),
    path('pet/<int:id>/care_plans/', views.view_care_plans, name='view_care_plans'),
]

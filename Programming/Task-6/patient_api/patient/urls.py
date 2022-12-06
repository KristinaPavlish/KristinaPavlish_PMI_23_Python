from .views import patient_detail, patient_list, create_patient
from django.urls import path, re_path

urlpatterns = [
    path('patient/<int:patient_id>', patient_detail),
    path('patient', create_patient),
    path('patients', patient_list),
]
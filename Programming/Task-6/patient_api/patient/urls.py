from .views import patient_detail, patient_list, create_patient
from django.urls import path

urlpatterns = [
    path('patients', patient_list),
    path('patient/<int:patient_id>', patient_detail),
    path('patient', create_patient),

]
# GET /patients
# DELETE /patient/{patient_id}
# GET  /patients/{patient_id}
# PUT  /patients/{patient_id} -> UPDATE PATIENT(IN BODY SOME MODEL)
# POST /patients/{patient_id} -> CREATE NEW PATIENT(IN BODY SOME MODEL)
"""@api_view(['GET', 'POST'])
# POST api/patient body { property for creation}
def create_patient(request):

@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request):"""

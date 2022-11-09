from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Patients

# GET api/patient/{patient_id}
def get_patient(request, patient_id):
    return HttpResponse("You're looking at question %s." % patient_id)

# GET api/patient
def get_patients(request):
    return HttpResponse(" You're at the patient index.")

@api_view(['GET', 'POST'])
# POST api/patient body { property for creation}
def create_patient(request):
    patient_1 = Patients();
    patient_1.Patients.patient_name = "afassad"
    tutorials = [patient_1]
    if request.method == 'GET':
        patient_serializer = PatientSerializer(tutorials, many=True)
        return JsonResponse(patient_serializer.data, safe=False)

    elif request.method == 'POST':
        patient_serializer = PatientSerializer(tutorials, many=True)
        return JsonResponse(patient_serializer.data, safe=False)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
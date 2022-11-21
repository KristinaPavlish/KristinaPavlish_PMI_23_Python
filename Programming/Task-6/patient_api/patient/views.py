import json

from django.http import HttpResponse
from rest_framework.decorators import api_view
from .patient_db_service import PatientService


# GET /patients
# DELETE /patient/{patient_id}
# GET  /patients/{patient_id}
# PUT  /patients/{patient_id} -> UPDATE PATIENT(IN BODY SOME MODEL)
# POST /patients/{patient_id} -> CREATE NEW PATIENT(IN BODY SOME MODEL)

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, patient_id):

    if request.method == 'DELETE':
        patient_service = PatientService()
        if patient_service.get_by_id(patient_id) == "[]":
            return HttpResponse("No such patient", status=400)
        else:
            patient_service.delete_patient_by_id(patient_id)
            return HttpResponse("Patient has been successfully deleted.", status=200)

    elif request.method == 'GET':
        patient_service = PatientService()
        if patient_service.get_by_id(patient_id) == "[]":
            return HttpResponse("No such patient", status=400)
        else:
            return HttpResponse(patient_service.get_by_id(patient_id))

    elif request.method == 'PUT':
        patient_service = PatientService()

        if patient_service.get_by_id(patient_id) == "[]":
            return HttpResponse("No such patient", status=400)

        if str(request.body) == "b''":
            return HttpResponse("Model is not provided", status=400)
        try:
            patient_service.put_patient(patient_id, Payload(request.body))
            patient_service.validate(patient_service.get_by_id(patient_id))
        except Exception as e:
            return HttpResponse("Method is incorrect: " + str(e), status=400)
        return HttpResponse(patient_service.get_by_id(patient_id))


@api_view(['GET'])
def patient_list(request):
    if request.method == 'GET':
        patient_service = PatientService()
        return HttpResponse(patient_service.get_patients())


@api_view(['POST'])
def create_patient(request):
    if request.method == 'POST':
        patient_service = PatientService()
        if str(request.body) == "b''":
            return HttpResponse("Model is not provided", status=400)
        try:
            patient_service.post_patient(Payload(request.body))
            patient_service.validate(patient_service.get_patients())
        except Exception as e:
            return HttpResponse("Method is incorrect: " + str(e), status=400)
        return HttpResponse(patient_service.get_patients())

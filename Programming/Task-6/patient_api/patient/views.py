import json

from django.http import HttpResponse
from rest_framework.decorators import api_view
from .patient_db_service import PatientService

# GET /patients
# DELETE /patient/{patient_id}
# GET  /patients/{patient_id}
# PUT  /patients/{patient_id} -> UPDATE PATIENT(IN BODY SOME MODEL)
# POST /patients/{patient_id} -> CREATE NEW PATIENT(IN BODY SOME MODEL)
OFFS = 0


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
        count_in_dict = {"count": size_of_all_patient()}
        patient_service = PatientService()
        limit = request.GET.get("limit")
        offset = request.GET.get("offset")
        sort = request.GET.get("sort")
        sort_by_desc = request.GET.get("sort_by_desc")
        to_search = request.GET.get("search")
        if limit is None:
            limit = size_of_all_patient()
        if offset is None:
            offset = OFFS
        try:
            if to_search is None:
                if sort is None and sort_by_desc is None:
                    return HttpResponse(patient_service.get_patients_without_any_order(limit, offset) + str(count_in_dict))

                if sort is None and sort_by_desc is not None:
                    return HttpResponse(patient_service.get_patients_order_by_desc(limit, offset, sort_by_desc) + str(count_in_dict))

                if sort_by_desc is None and sort is not None:
                    return HttpResponse(
                        patient_service.get_patients_order_by(limit, offset, sort) + str(count_in_dict))
            else:
                if sort is None and sort_by_desc is None:
                    return HttpResponse(
                        patient_service.search_without_sort(limit, offset, to_search) + str(count_in_dict))
                if sort is not None and sort_by_desc is None:
                    return HttpResponse(
                        patient_service.search_sort(limit, offset, sort, to_search) + str(count_in_dict))
                if sort is None and sort_by_desc is not None:
                    return HttpResponse(
                        patient_service.search_sort_desc(limit, offset, sort_by_desc, to_search) + str(count_in_dict))
            patient_service = PatientService()
        except Exception as e:
            return HttpResponse("Method is incorrect: " + str(e), status=400)
        return HttpResponse(patient_service.get_patients(limit, offset, sort, sort_by_desc) + str(count_in_dict))


def size_of_all_patient():
    patient_service = PatientService()
    str_count = str(patient_service.count_patient())
    to_dict = json.loads(str_count)
    elem = to_dict[0]
    return elem['COUNT(patient_id)']


@api_view(['POST'])
def create_patient(request):
    if request.method == 'POST':
        patient_service = PatientService()
        if str(request.body) == "b''":
            return HttpResponse("Model is not provided", status=400)
        try:
            patient_service.post_patient(Payload(request.body))
            size_of = size_of_all_patient()
            patient_service.validate(patient_service.get_patients_without_any_order(int(size_of), 0))
        except Exception as e:
            return HttpResponse("Method is incorrect: " + str(e), status=400)
        size_of = size_of_all_patient()
        return HttpResponse(patient_service.get_patients_without_any_order(int(size_of), 0))

import socket

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from covid19.models import Covid19India, CovidVaccineStatewise, StateWiseTestingDetails
from covid19.serializers import Covid19IndiaSerializer, CovidVaccineStatewiseSerializer, \
    StateWiseTestingDetailsSerializer
from covid19.validators import validate_get_date_info, validate_get_state_info, validate_pinpoint_state


def index(request):
    return Response("Hello, world. You're at the covid19 index.")


def _get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@api_view(['GET'])
def get_date_info(request):
    if _get_client_ip(request) != socket.gethostbyname('whispering-lake-44932.herokuapp.com'):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    request_validation = validate_get_date_info(request)
    if not request_validation["success"]:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            "details": request_validation["details"],
            "errors": request_validation["errors"]
        })

    date = request.data["date"]

    q1 = Covid19India.objects.filter(date=date)
    q1_serializer = Covid19IndiaSerializer(q1, many=True)

    q2 = CovidVaccineStatewise.objects.filter(updated_on=date)
    q2_serializer = CovidVaccineStatewiseSerializer(q2, many=True)

    q3 = StateWiseTestingDetails.objects.filter(date=date)
    q3_serializer = StateWiseTestingDetailsSerializer(q3, many=True)

    response_json = {
        "date": date,
        "covid_19_india": q1_serializer.data,
        "covid_vaccine_statewise": q2_serializer.data,
        "state_wise_testing_details": q3_serializer.data
    }
    return Response(response_json, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_state_info(request):
    request_validation = validate_get_state_info(request)
    if not request_validation["success"]:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            "details": request_validation["details"],
            "errors": request_validation["errors"]
        })

    state = request.data["state"]

    q1 = Covid19India.objects.filter(state_union_territory=state).order_by('date')
    q1_serializer = Covid19IndiaSerializer(q1, many=True)

    q2 = CovidVaccineStatewise.objects.filter(state=state).order_by('updated_on')
    q2_serializer = CovidVaccineStatewiseSerializer(q2, many=True)

    q3 = StateWiseTestingDetails.objects.filter(state=state).order_by('date')
    q3_serializer = StateWiseTestingDetailsSerializer(q3, many=True)

    response_json = {
        "state": state,
        "covid_19_india": q1_serializer.data,
        "covid_vaccine_statewise": q2_serializer.data,
        "state_wise_testing_details": q3_serializer.data
    }
    return Response(response_json, status=status.HTTP_200_OK)


@api_view(['GET'])
def pinpoint_state(request):
    request_validation = validate_pinpoint_state(request)
    if not request_validation["success"]:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            "details": request_validation["details"],
            "errors": request_validation["errors"]
        })

    state = request.data["state"]
    date = request.data["date"]

    q1 = Covid19India.objects.filter(state_union_territory=state, date=date)
    q1_serializer = Covid19IndiaSerializer(q1, many=True)

    q2 = CovidVaccineStatewise.objects.filter(state=state, updated_on=date)
    q2_serializer = CovidVaccineStatewiseSerializer(q2, many=True)

    q3 = StateWiseTestingDetails.objects.filter(state=state, date=date)
    q3_serializer = StateWiseTestingDetailsSerializer(q3, many=True)

    response_json = {
        "state": state,
        "date": date,
        "covid_19_india": q1_serializer.data,
        "covid_vaccine_statewise": q2_serializer.data,
        "state_wise_testing_details": q3_serializer.data
    }
    return Response(response_json, status=status.HTTP_200_OK)

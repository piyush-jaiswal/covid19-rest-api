from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from covid19.models import Covid19India, CovidVaccineStatewise, StateWiseTestingDetails
from covid19.serializers import Covid19IndiaSerializer, CovidVaccineStatewiseSerializer, \
    StateWiseTestingDetailsSerializer
from covid19.validators import validate_get_date_info, validate_get_state_info, validate_pinpoint_state


@api_view(['GET'])
def index(request):
    return Response("Hello, you're at the Covid19 index.")


@api_view(['GET'])
def get_date_info(request):
    request_validation = validate_get_date_info(request)
    if not request_validation["success"]:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            "details": request_validation["details"],
            "errors": request_validation["errors"]
        })

    date = request.query_params["date"]

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

    state = request.query_params["state"]

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

    state = request.query_params["state"]
    date = request.query_params["date"]

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

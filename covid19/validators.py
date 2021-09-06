from covid19 import serializers


def _get_validation_result(request, serializer):
    validation = serializer(data=request.data)
    return {
        "success": validation.is_valid(),
        "details": None if validation.is_valid() else "Bad Request Body",
        "errors": validation.errors
    }


def validate_get_date_info(request):
    return _get_validation_result(request, serializers.GetDateInfoRequestSerializer)


def validate_get_state_info(request):
    return _get_validation_result(request, serializers.GetStateInfoRequestSerializer)


def validate_pinpoint_state(request):
    return _get_validation_result(request, serializers.PinpointStateRequestSerializer)

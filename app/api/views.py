from rest_framework.views import APIView
from rest_framework.response import Response
from .func import validation_function
import json

class Validity_Api_1(APIView):
    """Test APIView"""
    validation_function = validation_function()

    def post(self, request):
        values = request.data['values']
        supported_values= request.data['supported_values']
        invalid_trigger = request.data['invalid_trigger']
        key = request.data['key']
        support_multiple = request.data['support_multiple']
        pick_first = request.data['pick_first']
        result = validation_function.validate_finite_values_entity(validation_function,values,supported_values,invalid_trigger,key,support_multiple,pick_first)

        return Response(json.loads(json.dumps(result)))

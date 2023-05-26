from rest_framework.views import APIView
from rest_framework.response import Response
from appointment.models import Establishments
from .serializers import *

# Create your views here.
class EstablishmentsApiView(APIView):
    def get(self, request, format=None):
        queryset = Establishments.objects.all()
        serializer_data = EstablishmentsSerializer(queryset, many=True).data
        return Response(serializer_data)

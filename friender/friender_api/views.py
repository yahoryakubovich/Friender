from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from appointment.models import Establishments
from .serializers import *
from django.urls import reverse


# Create your views here.
# class EstablishmentsApiView(APIView):
#
# def get_object(self, pk):
#     try:
#         return Establishments.objects.get(pk=pk)
#     except Establishments.DoesNotExist:
#         raise Http404
#
# def get(self, request, format=None):
#     queryset = Establishments.objects.all()
#     serializer_data = EstablishmentsSerializer(queryset, many=True).data
#     return Response(serializer_data)
#
# def post(self, request, format=None):
#     serializer = EstablishmentsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# def put(self, request, pk, format=None):
#     place = Establishments.objects.get(id=pk)
#     serializer = EstablishmentsSerializer(place, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstablishmentsListAPIView(generics.ListCreateAPIView):
    queryset = Establishments.objects.all()
    serializer_class = EstablishmentsSerializer


class EstablishmentsListAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Establishments.objects.all()
    serializer_class = EstablishmentsSerializer


class HobbiesListAPIView(generics.ListCreateAPIView):
    queryset = Hobbies.objects.all()
    serializer_class = HobbiesSerializer


class HobbiesListAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hobbies.objects.all()
    serializer_class = HobbiesSerializer

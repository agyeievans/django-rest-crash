from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django_rest.serializers import StudentSerializer
from django_rest.models import Student

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'John',
            'age': 23
        }
        return Response(data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django_rest.serializers import StudentSerializer
from django_rest.models import Student

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        # this is for post request
        # data = {
        #     'username': 'John',
        #     'age': 23
        # }

        # this is for get request
        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)

        return Response(data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
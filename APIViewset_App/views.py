from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from APIViewset_App.models import Student
from APIViewset_App.serializer import StudentSerializer


# Create your views here.
class StudentViewset(viewsets.ViewSet):
    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_id(self, id):
        return get_object_or_404(Student, id=id)
        # try:
        #     return Student.objects.get(id=id)
        # except self.Student.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stud = self.get_id(id)
            serializer = StudentSerializer(stud)
            return Response(serializer.data)

    def update(self, request, pk):
        id = pk
        stud = self.get_id(id)
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        stud = self.get_id(id)
        stud.delete()
        return Response({'msg': 'Data deleted!'}, status=status.HTTP_204_NO_CONTENT)

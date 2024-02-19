from rest_framework import serializers

from APIViewset_App.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('stud_id', 'stud_name', 'dept')

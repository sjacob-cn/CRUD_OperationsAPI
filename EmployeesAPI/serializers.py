from rest_framework import serializers
from .models import Employees
class EmployeesAPISerializer(serializers.ModelSerializer):

    class Meta:
        model=Employees
        fields='__all__'
        
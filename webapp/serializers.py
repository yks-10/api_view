from rest_framework import serializers 
from . models import employees

class employeesSerializer(serializers.ModelSerializer):
	class Meta:
		model=employees 
		fields='__all__' #{"first_name","last_name"}


 
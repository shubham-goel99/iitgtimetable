from rest_framework import serializers
from models import timetable

class TimetableSerializer(serializers.ModelSerializer):
	class Meta:
		model = timetable
		fields='__all__'
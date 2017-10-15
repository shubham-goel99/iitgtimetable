# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from .serializers import TimetableSerializer
from .models import timetable
from django.http import JsonResponse
# Create your views here.


# def timetable(request):
	# return render(request,'timetable/query.html')


# def result(request,day,slot):
	# return render(request,'timetable/result.html',{
		# 'day': day,
		# 'slot' : slot,
		# })


class timetables(generics.ListCreateAPIView):
	queryset = timetable.objects.all()
	serializer_class = TimetableSerializer

def result(request,pk):
	day1=get_object_or_404(timetable, id = pk)
	serializer = TimetableSerializer(day1)
	return JsonResponse(serializer.data)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class timetable(models.Model):
	slot1=models.CharField(max_length=35)
	slot2=models.CharField(max_length=35)
	slot3=models.CharField(max_length=35)
	slot4=models.CharField(max_length=35)
	slot5=models.CharField(max_length=35)

	def __str__(self):
		return 'slot 1- '+self.slot1+'\n'+'slot 2- '+self.slot2+'\n'+'slot 3- '+self.slot3+'\n'+'slot 4- '+self.slot4+'\n'+'slot 5 -'+self.slot5
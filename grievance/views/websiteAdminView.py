#common django imports
from django.shortcuts import render
from django.views import generic

#import decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from grievance.customDecorator import allocationTeam_required

#import models
from grievance.models import *

#import function for date and time
from datetime import datetime

class changeDeadlineView(generic.View):
	def get(self, request, *args, **kwargs):
		
		if Deadline.objects.filter().count() == 0:
			for i in range(3):
				Deadline.objects.create(attempt = i+1, date = datetime.now())

		params = {
			'deadline1' : Deadline.objects.get(attempt = 1).date,
			'deadline2' : Deadline.objects.get(attempt = 2).date,
			'deadline3' : Deadline.objects.get(attempt = 3).date,
			}
			
		#TODO return render(request, "", params)

	def post(self, request, *args, **kwargs):
		deadline[1] = request.POST.get("deadline1")
		deadline[2] = request.POST.get("deadline2")
		deadline[3] = request.POST.get("deadline3")

		for i in range(3):
			# print(i, " ", deadline[i])
			deadlineObject = Deadline.objects.get(attempt = i+1)
			deadlineObject.date = deadline[i+1]
			deadlineObject.save()

		return HttpResponseRedirect('/ps-grievance/redirect/')

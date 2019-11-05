#common django imports
from django.shortcuts import render
from django.views import generic

#import decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from grievance.customDecorator import allocationTeam_required

#import models
from grievance.models import *
from grievance.views import constants as constants

def getStudentDetail(student_id):
	userProfile_object = UserProfile.objects.get(user=User.objects.get(username = student_id))
	informativeQueryForm_objects = InformativeQueryForm.objects.filter(student_id = userProfile_object)
	const = constants.Status.NOAPPLICATION.value
	attempt_status=[const,const,const]
	for i in informativeQueryForm_objects:
		attempt_status[i.attempt-1] = i.status
	print("\n\n\n\n\n")
	print(attempt_status)
	params = {
		'name' : userProfile_object.name,
		'student_id' : student_id,
		'cg' : userProfile_object.cg,
		'informativeQueryForm_objects' : informativeQueryForm_objects,
		'statuses' : attempt_status,
		'back': "/ps-grievance/redirect/",
	}

	return params

class ViewOnlyPSDStudentPageView(generic.View):
	def get(self, request, *args, **kwargs):
		student_id = kwargs['student_id']
		params = getStudentDetail(student_id)
		return render(request, "grievance/viewOnlyQueryPage.html", params)

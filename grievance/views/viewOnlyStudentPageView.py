#common django imports
from django.shortcuts import render
from django.views import generic

#import decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from grievance.customDecorator import not_student_required

#import models
from grievance.models import *

def getStudentDetail(student_id):
	userProfile_object = UserProfile.objects.get(user=User.objects.get(username = student_id))
	grievanceForm_object = GrievanceForm.objects.get(student_id = userProfile_object)
	applicationStatus_objects = ApplicationStatus.objects.filter(student_id = userProfile_object)
	numberOfAttempts = len(applicationStatus_objects)
	documents = getDocuments(grievanceForm_object)
	if documents:
		documentCount = len(documents)
	else:
		documentCount = 0
	# print("HELLO")
	# print(grievanceForm_object.document1)
	params={
		'name' : userProfile_object.name,
		'student_id' : student_id,
		'cg' : userProfile_object.cg,
		'applcationStatusObjects' : applicationStatus_objects,
		'grievanceFormObject' : grievanceForm_object,
		'priority' : grievanceForm_object.priority,
		'numberOfAttempts' : numberOfAttempts,
		'back' : '/PS2/redirect',
		'documentCount': documentCount,
		'documents': documents,
	}

	return params

def getDocuments(grievanceForm_object):
	documents = []
	documentCount = 0
	if grievanceForm_object.document1:
		documentCount+=1
		documents.append(grievanceForm_object.document1)
	if grievanceForm_object.document2:
		documentCount+=1
		documents.append(grievanceForm_object.document2)
	if grievanceForm_object.document3:
		documentCount+=1
		documents.append(grievanceForm_object.document3)
	if grievanceForm_object.document4:
		documentCount+=1
		documents.append(grievanceForm_object.document4)
	if grievanceForm_object.document5:
		documentCount+=1
		documents.append(grievanceForm_object.document5)
	return documents

@method_decorator([login_required, not_student_required], name='dispatch')
class ViewOnlyStudentPageView(generic.View):
	def get(self, request, *args, **kwargs):
		student_id = kwargs['student_id']
		params = getStudentDetail(student_id)
		return render(request, "grievance/viewOnlyStudentPage.html", params)

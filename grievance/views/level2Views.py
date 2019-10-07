#common django imports
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.http import HttpResponseRedirect

#import decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from grievance.customDecorator import cmo_or_ad_required

#import models
from grievance.models import *

#import views
from grievance.views import constants as constants


# @method_decorator([login_required,allocationTeam_required], name='dispatch') #TODO
class level2HomeView(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request,"grievance/level2HomePage.html")

	def post(self, request, *args, **kwargs):
		student_list = ApplicationStatus.objects.filter(level = 2, 
			publish = constants.Publish.UNPUBLISHED.value, ).exclude( status = constants.Status.PENDING.value)

		for student in student_list:
			student.publish = 1
			student.save()

		return HttpResponseRedirect('/ps-grievance/redirect/')

# @method_decorator([login_required, allocationTeam_required], name='dispatch') #TODO
class level2RequestView(generic.View):
	def get(self, request, *args, **kwargs):

		typeOfRequest = kwargs["type"]
		if typeOfRequest == "pending":
			status = constants.Status.PENDING.value
			student_list = ApplicationStatus.objects.filter(level = 2, status=status ,).order_by('lastChangedDate')
		elif typeOfRequest == "approved":
			status = constants.Status.APPROVED.value
			student_list = ApplicationStatus.objects.filter(level = 2, status=status ,publish=constants.Publish.PUBLISHED.value).order_by('lastChangedDate')
		elif typeOfRequest == "rejected":
			status = constants.Status.REJECTED.value 
			student_list = ApplicationStatus.objects.filter(level = 2, status=status ,publish=constants.Publish.PUBLISHED.value).order_by('lastChangedDate')
		elif typeOfRequest == "unpublished":
			return self.getUnpublished()

		# user_object = request.user
		# user_profile_object = UserProfile.objects.get(user_id=user_object)

		# student_list = ApplicationStatus.objects.filter(level = 2, 
		# 	status=status ,).order_by('lastChangedDate')
		
		returnList=[]
		lowPriorityList=[]
		midPriorityList=[]
		highPriorityList=[]
		for student in student_list:
			dict1 = {
				"id":student.student_id.user.username,
				"name":student.student_id.name,
				"description":student.description
				}

			priority = GrievanceForm.objects.get(student_id=student.student_id).priority
			if priority == constants.Priority.LOW.value : 
				lowPriorityList.append(dict1) 
			elif priority == constants.Priority.MEDIUM.value :
				midPriorityList.append(dict1)
			else:
				highPriorityList.append(dict1)

		returnList.append(lowPriorityList)
		returnList.append(midPriorityList)
		returnList.append(highPriorityList)
		# print(returnList)
		return JsonResponse(returnList, safe=False)

	def getUnpublished(self):
		approvedList = []
		student_list = ApplicationStatus.objects.filter(level = 2, status=constants.Status.APPROVED.value  ,publish=constants.Publish.UNPUBLISHED.value).order_by('lastChangedDate')
		for student in student_list:
			dict1 = {
				"id":student.student_id.user.username,
				"name":student.student_id.name,
				"description":student.description
				}

			# priority = GrievanceForm.objects.get(student_id=student.student_id).priority 
			approvedList.append(dict1) 

		# rejected unpublished list
		rejectedList = []
		student_list = ApplicationStatus.objects.filter(level = 2, status=constants.Status.REJECTED.value  ,publish=constants.Publish.UNPUBLISHED.value).order_by('lastChangedDate')
		for student in student_list:
			dict1 = {
				"id":student.student_id.user.username,
				"name":student.student_id.name,
				"description":student.description
				}

			# priority = GrievanceForm.objects.get(student_id=student.student_id).priority 
			rejectedList.append(dict1) 

		returnList = []
		returnList.append(approvedList)
		returnList.append(rejectedList)

		return JsonResponse(returnList, safe=False)

# @method_decorator([login_required, allocationTeam_required], name='dispatch')
class level2StudentView(generic.View):
	def get(self, request, *args, **kwargs):
		student_id = kwargs['student_id']
		userProfile_object = UserProfile.objects.get(user=User.objects.get(username = student_id))
		grievanceForm_object = GrievanceForm.objects.get(student_id = userProfile_object)
		applicationStatus_objects = ApplicationStatus.objects.filter(student_id = userProfile_object)
		numberOfAttempts = len(applicationStatus_objects)
		# print("HELLO")
		# print(grievanceForm_object.document1)
		params={
			'name' : userProfile_object.name,
			'student_id' : student_id,
			'applcationStatusObjects' : applicationStatus_objects,
			'grievanceFormObject' : grievanceForm_object,
			'priority' : grievanceForm_object.priority,
			'numberOfAttempts' : numberOfAttempts,

		}
		return render(request,"grievance/level2StudentPage.html",params)

	def post(self, request, *args, **kwargs):
		student_id = kwargs['student_id']
		attempt = request.POST.get('attempt') 
		# attempt = 1
		userProfile_object = UserProfile.objects.get(user=User.objects.get(username = student_id))
		applicationStatus_object = ApplicationStatus.objects.get(student_id = userProfile_object, attempt =attempt)

		if applicationStatus_object.status == constants.Status.PENDING.value : 
			newStation = request.POST.get("newStation")
			level2comment = request.POST.get("remarks")
			publish = request.POST.get("publish")

			applicationStatus_object.level2Comment = level2comment
			applicationStatus_object.publish = publish
			if request.POST.get('button') == "approve":
				applicationStatus_object.newStation = newStation
				applicationStatus_object.status = constants.Status.APPROVED.value
			else :
				applicationStatus_object.status = constants.Status.REJECTED.value

			applicationStatus_object.save()

		return HttpResponseRedirect('/ps-grievance/redirect/')
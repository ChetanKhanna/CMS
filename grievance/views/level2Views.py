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


# @method_decorator([login_required], name='dispatch') #TODO
class level2HomeView(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request,"grievance/level2HomePage.html")

# @method_decorator([login_required, cmo_or_ad_required], name='dispatch') #TODO
class level2RequestView(generic.View):
	def get(self, request, *args, **kwargs):

		typeOfRequest = kwargs["type"]
		if typeOfRequest == "pending":
			status = constants.Status.PENDING.value
		elif typeOfRequest == "approved":
			status = constants.Status.APPROVED.value
		else:
			status = constants.Status.REJECTED.value 

		# user_object = request.user
		# user_profile_object = UserProfile.objects.get(user_id=user_object)

		student_list = ApplicationStatus.objects.filter(level = 2, 
			status=status ,).order_by('lastChangedDate')
		
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
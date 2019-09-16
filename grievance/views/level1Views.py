#common django imports
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.http import HttpResponseRedirect

#import decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from grievance.customDecorator import cmo_or_ad_required, ad_required

#import models
from grievance.models import *

#import views
from grievance.views import constants as constants
from grievance.views import studentHomeView


@method_decorator([login_required, cmo_or_ad_required], name='dispatch')
class level1HomeView(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request,"grievance/level1HomePage.html")


@method_decorator([login_required, cmo_or_ad_required], name='dispatch')
class level1RequestView(generic.View):
	def get(self, request, *args, **kwargs):

		typeOfRequest = kwargs["type"]
		if(typeOfRequest == "pending"):
			level = 1
		else:
			level = 2

		user_object = request.user
		user_profile_object = UserProfile.objects.get(user_id=user_object)
		campus =  user_profile_object.campus

		if user_profile_object.token == constants.UserType.CMO.value:
			natureOfQuery = constants.NatureOfQuery.MEDICAL.value
		else:
			natureOfQuery = constants.NatureOfQuery.NONMEDICAL.value

		student_list = ApplicationStatus.objects.filter(campus = campus, level = level, 
			 natureOfQuery = natureOfQuery, attempt=1).order_by(
			'lastChangedDate')
		
		returnList=[]
		for student in student_list:
			dict1 = {
			"id":student.student_id.user.username,
			"name":student.student_id.name,
			"description":student.description
			}
			returnList.append(dict1) 
		# print(returnList)
		return JsonResponse(returnList, safe=False)

@method_decorator([login_required, cmo_or_ad_required], name='dispatch')
class level1StudentView(generic.View):
	def get(self, request, *args, **kwargs):
		student_id = kwargs['student_id']
		userProfile_object = UserProfile.objects.get(user=User.objects.get(username = student_id))
		ApplicationStatus_object = ApplicationStatus.objects.get(student_id = userProfile_object,attempt =1)
		params={
			'name' : userProfile_object.name,
			'student_id' : student_id,
			'allocatedStation' : 'remove it',
			'applicationDate' : ApplicationStatus_object.lastChangedDate,
			'description': ApplicationStatus_object.description,
		}
		return render(request,"grievance/cmoStudentPage.html",params)
	def post(self, request, *args, **kwargs):
		student_id = kwargs['student_id']
		userProfile_object = UserProfile.objects.get(user=User.objects.get(username = student_id))
		ApplicationStatus_object = ApplicationStatus.objects.get(student_id = userProfile_object, attempt =1)
		grievanceForm_object = GrievanceForm.objects.get(student_id = userProfile_object)

		priority = request.POST.get("priority")
		level1comment = request.POST.get("remarks")

		grievanceForm_object.priority = priority

		ApplicationStatus_object.level1Comment = level1comment
		ApplicationStatus_object.level = 2
		ApplicationStatus_object.status = constants.Status.PENDING.value

		ApplicationStatus_object.save()
		grievanceForm_object.save()

		return HttpResponseRedirect('/ps-grievance/redirect/')

# # TODO
# class level1StudentDetails(generic.View):
# 	def post(self, request, *args, **kwargs):
# 		student_id = kwargs[student_id]
# 		userProfile_object = UserProfile.objects.get(user=User.objects.get(username = student_id))
# 		ApplicationStatus_object = ApplicationStatus.objects.get(student_id = userProfile_object)
		
# 		priority = request.POST.get("priority")
# 		level1comment = request.POST.get("remarks")
		
# 		ApplicationStatus_object.priority = priority
# 		ApplicationStatus_object.level1comment = level1comment
# 		ApplicationStatus_object.save()

# 		return render(request,"grievance/level1HomePage.html")

@method_decorator([login_required, cmo_or_ad_required], name='dispatch')
class level1StudentStatusView(generic.View):
	def get(self, request, *args, **kwargs):

		student_id = kwargs['student_id']
		student = User.objects.get(username = student_id)
		details = studentHomeView.studentHomeView().getDetails(student)
		return render (request, "grievance/grievanceForm.html", details)

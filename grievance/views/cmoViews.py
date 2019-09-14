#common django imports
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse

#import decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from grievance.customDecorator import cmo_or_ad_required

#import models
from grievance.models import ApplicationStatus, UserProfile

#import views
from grievance.views import constants as constants


@method_decorator([login_required, cmo_or_ad_required], name='dispatch')
class level1HomeView(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request,"grievance/cmoHomePage.html")


@method_decorator([login_required, cmo_or_ad_required], name='dispatch')
class level1RequestView(generic.View):
	def get(self, request, *args, **kwargs):

		typeOfRequest = kwargs["type"]
		if(typeOfRequest == "pending"):
			level=1
		else:
			level=2

		user_object = request.user
		user_profile_object = UserProfile.objects.get(user_id=user_object)
		campus =  user_profile_object.campus

		if user_profile_object.token == constants.UserType.CMO.value:
			natureOfQuery = constants.NatureOfQuery.MEDICAL.value
		else:
			natureOfQuery = constants.NatureOfQuery.NONMEDICAL.value

		student_list = ApplicationStatus.objects.filter(campus = campus, level = level, 
			natureOfQuery = natureOfQuery).order_by(
			'lastChangedDate')
		
		returnList=[]
		for student in student_list:
			dict1 = {
			"id":student.student_id.user.username,
			"name":student.student_id.name,
			"description":student.discription
			}
			returnList.append(dict1) 
		# print(returnList)
		return JsonResponse(returnList, safe=False)

@method_decorator([login_required, cmo_or_ad_required], name='dispatch')
class level1StudentView(generic.View):
	def get(self, request, *args, **kwargs):
		params={'name':"name222"}
		return render(request,"grievance/cmoStudentPage.html",params)

#TODO
# class level1StudentDetails(generic.View):
# 	def get(self, request, *args, **kwargs):
# 		student_id = kwargs[student_id]

#common django imports
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse

#import decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from grievance.customDecorator import cmo_required

#import models
from grievance.models import ApplicationStatus

#import views
from grievance.views import constants as constants


# @method_decorator([login_required,cmo_required], name='dispatch')
class cmoHomeView(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request,"grievance/cmoHomePage.html")


# @method_decorator([login_required,cmo_required], name='dispatch')
class cmoRequestView(generic.View):
	def get(self, request, *args, **kwargs):

		typeOfRequest = kwargs["type"]
		if(typeOfRequest == "pending"):
			level=1
		else:
			level=2

		# TODO cmo_object = request.user
		campus = 0# TODO cmo_object.campus

		student_list = ApplicationStatus.objects.filter(campus = campus, level = level, 
			natureOfQuery = constants.NatureOfQuery.MEDICAL.value).order_by(
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

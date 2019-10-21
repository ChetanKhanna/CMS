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
		current_user = request.user
		userProfile_object = UserProfile.objects.get(user = current_user)

		if userProfile_object.token == constants.UserType.CMO.value:
			return render(request,"grievance/level1HomePage.html")
		elif userProfile_object.token == constants.UserType.AD.value:
			return render(request,"grievance/adHomePage.html")

# class adHomeView(generic.TemplateView):
# 	def get(self, request, *args, **kwargs):
# 		return render(request,"grievance/adHomePage.html")

@method_decorator([login_required, cmo_or_ad_required], name='dispatch')
class level1RequestView(generic.View):
	def get(self, request, *args, **kwargs):

		user_object = request.user
		user_profile_object = UserProfile.objects.get(user_id=user_object)
		campus =  user_profile_object.campus

		typeOfRequest = kwargs["type"]
		print(typeOfRequest)
		if typeOfRequest == "medical":
			natureOfQuery = constants.NatureOfQuery.MEDICAL.value
			student_list = ApplicationStatus.objects.filter(campus = campus,
			 	natureOfQuery = natureOfQuery).order_by('-lastChangedDate')
		elif typeOfRequest == "informative":
			print("sdfj")
		else:
			if typeOfRequest == "pending":
				level = 1
			elif typeOfRequest == "forwarded":
				level = 2

			if user_profile_object.token == constants.UserType.CMO.value:
				natureOfQuery = constants.NatureOfQuery.MEDICAL.value
			else:
				natureOfQuery = constants.NatureOfQuery.NONMEDICAL.value

			student_list = ApplicationStatus.objects.filter(campus = campus, level = level, 
				 natureOfQuery = natureOfQuery, attempt=1).order_by('-lastChangedDate')
		
		returnList=[]
		for student in student_list:
			dict1 = {
				"id":student.student_id.user.username,
				"name":student.student_id.name,
				"description":student.description,
				"status" : constants.Status(student.status).name,
				"level" : student.level,
				"attempt" : student.attempt,
				"date": str(student.lastChangedDate.date()) + " " + str(student.lastChangedDate.time())[0:8],
			}
			returnList.append(dict1) 
		print(returnList)
		return JsonResponse(returnList, safe=False)

@method_decorator([login_required, cmo_or_ad_required], name='dispatch')
class level1StudentView(generic.View):
	def get(self, request, *args, **kwargs):
		student_id = kwargs['student_id']
		userProfile_object = UserProfile.objects.get(user=User.objects.get(username = student_id))
		ApplicationStatus_object = ApplicationStatus.objects.get(student_id = userProfile_object,attempt =1)
		grievanceForm_object = GrievanceForm.objects.get(student_id = userProfile_object)
		documents = self.getDocuments(grievanceForm_object)
		if documents:
			documentCount = len(documents)
		else:
			documentCount = 0
		params={
			'name' : userProfile_object.name,
			'student_id' : student_id,
			'allocatedStation' : grievanceForm_object.allocatedStation,
			'applicationDate' : ApplicationStatus_object.lastChangedDate,
			'description': ApplicationStatus_object.description,
			'documentCount': documentCount,
			'documents': documents,
			'back': "/ps-grievance/level1/",
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


	def getDocuments(self, grievanceForm_object):
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


@method_decorator([login_required, cmo_or_ad_required], name='dispatch')
class level1StudentStatusView(generic.View):
	def get(self, request, *args, **kwargs):

		student_id = kwargs['student_id']
		student = User.objects.get(username = student_id)
		details = studentHomeView.studentHomeView().getDetails(student)
		return render (request, "grievance/grievanceForm.html", details)


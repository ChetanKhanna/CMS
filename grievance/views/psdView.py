from django.shortcuts import render
import os
from django.conf import settings
from django.views import generic
from django.http import HttpResponse

from grievance.views import date

BASE_DIR = settings.BASE_DIR


class updateLastSubmissionDate(generic.TemplateView):

	template_name = 'grievance/date.html'

	def post(self, request, *args, **kwargs):
		print("old date")
		print(date.datee)
		newDate = request.POST.get("date")
		jsFile = os.path.join(BASE_DIR, 'grievance/static/grievance/js/date.js')
		print(newDate)
		with open(jsFile, mode='w') as file:
			file.write("var date=\""+newDate+"\";")
			print("Hellloooo")
		pyFile = os.path.join(BASE_DIR, 'grievance/views/date.py')
		with open(pyFile, mode='w') as file:
			file.write("datee=\""+newDate+"\"")
		return HttpResponse('OK')

class PSDHomeView(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request, 'grievance/level1HomePage.html')

class PSDRequestView(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		user_object = request.user
		user_profile_object = UserProfile.objects.get(user_id = user_object)
		campus =  user_profile_object.campus
		status = constants.Status.PENDING.value
		# typeOfRequest = kwargs["type"]

		student_list = ApplicationStatus.objects.filter(campus = campus, status = status,).order_by('-lastChangedDate')
		
		returnList=[]
		for student in student_list:
			dict1 = {
				"id":student.student_id.user.username,
				"name":student.student_id.name,
				"status" : constants.Status(student.status).name,
				"attempt" : student.attempt,
				"date": str(student.lastChangedDate.date()) + " " + str(student.lastChangedDate.time())[0:8],
			}
			returnList.append(dict1) 
		# print(returnList)
		return JsonResponse(returnList, safe=False)
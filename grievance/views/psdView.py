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

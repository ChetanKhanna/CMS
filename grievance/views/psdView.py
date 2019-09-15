import os
from django.conf import settings
from django.views import generic
from django.http import HttpResponse


BASE_DIR = settings.BASE_DIR


class updateLastSubmissionDate(generic.TemplateView):

	template_name = 'grievance/date.html'

	def post(self, request, *args, **kwargs):
		newDate = request.POST.get("date")
		jsFile = os.path.join(BASE_DIR, 'grievance/static/grievance/js/date.js')
		with open(jsFile, mode='w') as file:
			file.write("var date=\""+newDate+"\";")
		return HttpResponse('OK')

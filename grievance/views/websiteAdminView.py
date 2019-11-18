#common django imports
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect

#import decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from grievance.customDecorator import allocationTeam_required
from django.contrib.admin.views.decorators import staff_member_required

#import models
from grievance.models import *

#import function for date and time
from datetime import datetime

#import function for random string to be used to set password
from django.utils.crypto import get_random_string

#import function to call management commands
from django.core import management

from django.conf import settings
BASE_DIR = settings.BASE_DIR

from django.core.files.storage import FileSystemStorage

@method_decorator([login_required, staff_member_required], name='dispatch')
class addUser(generic.TemplateView):

	def get(self, request, *args, **kwargs):
		params = {}
		return render(request, 'grievance/addUser.html', params)

	def post(self, request, *args, **kwargs):
		token = request.POST.get('userType')
		username = request.POST.get('userID')
		name = request.POST.get('name')
		contact = request.POST.get('contact')
		email = request.POST.get('email')
		campus = request.POST.get('campus')
		cg = request.POST.get('cg')
		# print(cg)
		user = None
		try:
			(user, created) = User.objects.get_or_create(username = username, email = email) 
			user.set_password(get_random_string(8))
			if token == 6:
				user.is_staff = True
				user.is_admin = True
				user.is_superuser = True
			user.save()
		except:
			pass

		try:
			(_, _) = UserProfile.objects.get_or_create(user = user, token = token, name = name, contact = contact, email = email, campus = campus, cg = cg)
		except:
			pass

		return HttpResponseRedirect('/PS2/redirect/')

@method_decorator([login_required, staff_member_required], name='dispatch')
class websiteAdminHomePageView(generic.TemplateView):

	def get(self, request, *args, **kwargs):
		params = {}
		return render(request, 'grievance/websiteAdminHomePage.html', params)

	def post(self, request, *args, **kwargs):
		# Generate Download file
		if request.POST.get("generateDownload"):
			management.call_command('downloadDatabaseAsCsv')
			return HttpResponse("<h1> wait for 5 mins and then click on download button")
		# DOWNLOAD
		if request.POST.get("download"):
			filename = 'databaseEntriesAsCsv.csv'
			path = os.path.join(BASE_DIR + '/media/', filename)
			file_path = os.path.join(settings.MEDIA_ROOT, path)
			file_path = path

			with open(file_path, 'rb') as fh:
				response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
				response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
				return response

			return HttpResponse("<h1> Download : Error please try again </h1>") 
		# ERASE
		elif request.POST.get("erase"):
			# Erase database
			management.call_command('clearModels')
			return redirect('/PS2/redirect')
		# UPLOAD
		elif request.FILES['myfile']: 
			fs = FileSystemStorage()
			# getting file 'data.csv'
			## Name of the file is hard-coded to accept only 'data.csv'.
			## No other file name would work.
			filename = 'data.csv'
			file = os.path.join(BASE_DIR+"/media", filename)				
			#DELETE data.csv IF ALREADY EXISTS
			if fs.exists(file):
				os.remove(file)
			# UPLOAD CODE
			myfile = request.FILES['myfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			# POPULATE DATABASE
			management.call_command('populateDB')
			return HttpResponse("<h1> Done, check log for more info </h1>")

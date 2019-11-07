#common django imports
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect

#import decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from grievance.customDecorator import allocationTeam_required

#import models
from grievance.models import *

#import function for date and time
from datetime import datetime

#import function for random string to be used to set password
from django.utils.crypto import get_random_string

class changeDeadlineView(generic.View):
	def get(self, request, *args, **kwargs):
		
		if Deadline.objects.filter().count() == 0:
			for i in range(3):
				Deadline.objects.create(attempt = i+1, date = datetime.now())
		return HttpResponseRedirect("/admin/grievance/deadline")

		params = {
			'deadline1' : Deadline.objects.get(attempt = 1).date,
			'deadline2' : Deadline.objects.get(attempt = 2).date,
			'deadline3' : Deadline.objects.get(attempt = 3).date,
			}
		return render(request, "grievance/websiteAdminChangeDeadline.html", params)

	def post(self, request, *args, **kwargs):
		deadline[1] = request.POST.get("deadline1")
		deadline[2] = request.POST.get("deadline2")
		deadline[3] = request.POST.get("deadline3")

		# print(request.POST.get("deadline1"))

		for i in range(3):
			# print(i, " ", deadline[i])
			deadlineObject = Deadline.objects.get(attempt = i+1)
			deadlineObject.date = deadline[i+1]
			deadlineObject.save()

		return HttpResponseRedirect('/ps-grievance/redirect/')


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

		return HttpResponseRedirect('/ps-grievance/redirect/')
from grievance.models import *

from functools import wraps
from django.http import HttpResponseRedirect

import grievance.views.constants as constants

def getUser(request):
	current_user = User.objects.get(username="20160080G") #TODO request.user
	return UserProfile.objects.get(user=current_user)

def student_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		profile = getUser(request)
		if profile.token == constants.UserType.STUDENT.value:
			return function(request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/redirect')

	return wrap

def cmo_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		profile = getUser(request)
		if profile.token == constants.UserType.CMO.value:
			return function(request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/redirect')

	return wrap

def ad_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		profile = getUser(request)
		if profile.token == constants.UserType.AD.value:
			return function(request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/redirect')

	return wrap

def allocationTeam_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		profile = getUser(request)
		if profile.token == constants.UserType.ALLOCATIONTEAM.value:
			return function(request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/redirect')

	return wrap

def superuser_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		profile = getUser(request)
		if profile.token == constants.UserType.SUPERUSER.value:
			return function(request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/redirect')

	return wrap

from grievance.models import *

from functools import wraps
from django.utils.decorators import method_decorator

from django.http import HttpResponseRedirect

from grievance.views import constants 

def getUser(request):
	current_user = request.user#User.objects.get(username="20160080G") #TODO request.user
	return UserProfile.objects.get(user=current_user)

def redirect():
	return HttpResponseRedirect('/ps-grievance/redirect/')

def student_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		profile = getUser(request)
		if profile.token == constants.UserType.STUDENT.value:
			return function(request, *args, **kwargs)
		else:
			return redirect()

	return wrap

def cmo_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		profile = getUser(request)
		if profile.token == constants.UserType.CMO.value:
			return function(request, *args, **kwargs)
		else:
			return redirect()

	return wrap

def ad_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		profile = getUser(request)
		if profile.token == constants.UserType.AD.value:
			return function(request, *args, **kwargs)
		else:
			return redirect()

	return wrap

def ad_or_level2_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		profile = getUser(request)
		if profile.token == constants.UserType.AD.value or profile.token == constants.UserType.ALLOCATIONTEAM.value:
			return function(request, *args, **kwargs)
		else:
			return redirect()

	return wrap

def level1_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		profile = getUser(request)
		if profile.token == constants.UserType.AD.value or profile.token == constants.UserType.CMO.value or profile.token == constants.UserType.PSD.value:
			return function(request, *args, **kwargs)
		else:
			return redirect()

	return wrap

def allocationTeam_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		profile = getUser(request)
		if profile.token == constants.UserType.ALLOCATIONTEAM.value:
			return function(request, *args, **kwargs)
		else:
			return redirect()

	return wrap

def superuser_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		profile = getUser(request)
		if profile.token == constants.UserType.SUPERUSER.value:
			return function(request, *args, **kwargs)
		else:
			return redirect()

	return wrap

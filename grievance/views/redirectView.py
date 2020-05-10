from django.shortcuts import redirect
from grievance.views import constants 
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from grievance.models import UserProfile


class RedirectView(generic.TemplateView):
	# request.GET call 
	def get(self, request, *args, **kwargs):
		# Check to see if user credentials in UserIdPassword table
		try:
			current_user = request.user
			user_object = UserProfile.objects.get(user=current_user)
			if user_object.token == constants.UserType.STUDENT.value:
				return redirect('/CMS/student')
			elif user_object.token == constants.UserType.CMO.value or user_object.token == constants.UserType.AD.value or user_object.token == constants.UserType.PSD.value:
				return redirect('/CMS/level1')
			elif user_object.token == constants.UserType.ALLOCATIONTEAM.value :
				return redirect('/CMS/level2')
			else:
				print("Unknow user logged in")
				return redirect('/CMS/login')
		except :
			# Check if user credentials match any admin/staff
			if current_user.is_superuser or current_user.is_staff:
				return redirect('/CMS/website-admin')
			# Redirect to login page for re-entry
			else:
				return redirect('/CMS/login')

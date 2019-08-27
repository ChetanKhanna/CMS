from django.shortcuts import render
from django.views import generic

import grievance.back_end_codes.constants as constants
import grievance.back_end_codes.cmo as b
# Create your views here.
class CMO(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		# current_user=request.user
		# if(current_user.is_authenticated):
		# 	if(UserType.objects.get(user=current_user).token == constants.UserType.CMO.value):
		# 		print("Success")k
		return b.CMO().get(self, request, args, kwargs)

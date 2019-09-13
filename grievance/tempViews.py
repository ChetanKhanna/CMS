from django.shortcuts import render
from django.views import generic

import grievance.views.constants as constants
import grievance.views.cmoViews as cmoViews
from django.shortcuts import redirect
# Create your views here.
class HomeView(generic.TemplateView):
	template_name = 'grievance/website_base.html'

class CMO(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		# current_user=request.user
		# if(current_user.is_authenticated):
		# 	if(UserType.objects.get(user=current_user).token == constants.UserType.CMO.value):
		# 		print("Success")k
		return cmoViews.CMO().get(self, request, args, kwargs)

class loginTimeoutRedirect(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return redirect('/ps-grievance/accounts/login')

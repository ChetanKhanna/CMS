from django.shortcuts import redirect
from django.views import generic

class loginTimeoutRedirect(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return redirect('/ps-grievance/accounts/login')
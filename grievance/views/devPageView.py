#common django imports
from django.shortcuts import render
from django.views import generic

class devPageView(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request, "grievance/devPage.html")
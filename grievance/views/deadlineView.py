# import models
from grievance.models import Deadline

# import datetime
from django.utils import timezone as datetime

# import for return
from django.http import JsonResponse
from django.views import generic

# import authenticator
from django.contrib.auth.decorators import login_required

def getDeadlines():
	deadline = []
	for i in range(1,4):
		rawDeadline = Deadline.objects.get(attempt = i).date
		deadline.append(str(rawDeadline.date()) + " " + str(rawDeadline.time()))
	# print("\n\ngetDeadlines()" )
	# print(deadline)
	return deadline

def checkDeadline(attemptNumber):
	currentDate = datetime.now()
	deadline = Deadline.objects.get(attempt = attemptNumber).date
	if currentDate > deadline:
		return 1
	else:
		return 0

def checkAllDeadline():
	expired = []
	currentDate = datetime.now()
	for i in range(1,4):
		expired.append(checkDeadline(i))
	# print("\n\ncheckAllDeadline()" )
	# print(expired)
	return expired


class showDeadlineInHeader(generic.View):
	def get(self, request, *args, **kwargs):
		currentDate = datetime.now()
		for i in range(1,4):
			deadline = Deadline.objects.get(attempt = i).date
			if currentDate < deadline:
				param = {
					'deadlineAttempt' : i,
					'deadline' : str(deadline.date()) + " " + str(deadline.time())
				}
				return JsonResponse(param, safe=False)
		
		param = {
			'deadlineAttempt' : 0,
			'deadline' : "passed"
		}
		return JsonResponse(param, safe=False)

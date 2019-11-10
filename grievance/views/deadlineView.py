# import models
from grievance.models import *

# import datetime
from django.utils import timezone as datetime

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

def showDeadlineInHeader():
	currentDate = datetime.now()
	for i in range(1,4):
		deadline = Deadline.objects.get(attempt = i).date
		if currentDate < deadline:
			return [i, str(deadline.date()) + " " + str(deadline.time())]
		
	return [3, str(deadline.date()) + " " + str(deadline.time())]

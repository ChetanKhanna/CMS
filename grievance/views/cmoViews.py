from grievance.models import ApplicationStatus
from grievance.views import constants as constants

from django.http import JsonResponse, HttpResponse
class CMO():
	def get(self, request, *args, **kwargs):
		# cmo_object = OtherUsers.objects.get(user_id = request.user)
		campus = 0#cmo_object.campus

		student_list = ApplicationStatus.objects.filter(campus = campus, level = 1, 
			natureOfQuery = constants.NatureOfQuery.MEDICAL.value)
		# list2=Student.objects.filter(student_id=student_list)
		# print(list2)
		# empty_list = list(student_list)
		empty_list=[]
		for student in student_list:
			print(student.student_id)
			empty_list.append(str(student))
			# print(, end=" ")
			# print(, end=" ")
			# print(, end=" ")
			# print(, end=" ")
		print(empty_list)
		# return HttpResponse(empty_list)
		return JsonResponse(empty_list, safe=False)
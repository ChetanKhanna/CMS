from grievance.models import ApplicationStatus
from grievance.views import constants as constants

from django.http import JsonResponse, HttpResponse
class CMO():
	def get(self, request, *args, **kwargs):

		typeOfRequest = request.GET.get("type")
		if(typeOfRequest == "pending"):
			level=1
		else:
			level=2

		# cmo_object = request.user
		campus = 0#cmo_object.campus

		student_list = ApplicationStatus.objects.filter(campus = campus, level = level, 
			natureOfQuery = constants.NatureOfQuery.MEDICAL.value)
		
		list1=[]
		for student in student_list:
			dict1 = {
			"id":student.student_id.user.username,
			"name":student.student_id.name,
			"description":student.discription
			}
			list1.append(dict1) 
		print("\n\n\n\n")
		print(list1)

		# empty_list=[]
		# for student in student_list:
		# 	print(student.student_id)
		# 	empty_list.append(str(student))
		# 	# print(, end=" ")
		# 	# print(, end=" ")
		# 	# print(, end=" ")
		# 	# print(, end=" ")
		# print(empty_list)
		# # return HttpResponse(empty_list)
		return JsonResponse(list1, safe=False)


	# def getApproved()
		
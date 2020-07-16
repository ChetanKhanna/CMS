# common django imports
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.core import serializers

# import decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from grievance.customDecorator import level1_required, ad_required

# import models
from grievance.models import *
from django.db.models import Q

# import views
from grievance.views import constants as constants
from grievance.views import studentHomeView, viewOnlyPSDStudentPageView, viewOnlyStudentPageView

# import datetime
from django.utils import timezone as datetime


@method_decorator([login_required, level1_required], name='dispatch')
class level1HomeView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        userProfile_object = UserProfile.objects.get(user=current_user)

        if userProfile_object.token == constants.UserType.CMO.value:
            return render(request,"grievance/cmoHomePage.html")
        elif userProfile_object.token == constants.UserType.AD.value:
            return render(request,"grievance/adHomePage.html")
        elif userProfile_object.token == constants.UserType.DEAN.value:
            return render(request,"grievance/adHomePage.html")
        else:
            return render(request,"grievance/psdHomePage.html")

# class adHomeView(generic.TemplateView):
#   def get(self, request, *args, **kwargs):
#       return render(request,"grievance/adHomePage.html")

@method_decorator([login_required, level1_required], name='dispatch')
class level1RequestView(generic.View):
    def get(self, request, *args, **kwargs):

        user_object = request.user
        user_profile_object = UserProfile.objects.get(user_id=user_object)
        campus =  user_profile_object.campus
        level = 1

        if user_profile_object.token == constants.UserType.PSD.value:
            return self.getPSDStudentList(request, kwargs["type"])

        if user_profile_object.token == constants.UserType.DEAN.value:
            return self.getDEANStudentList(request, kwargs["type"])

        typeOfRequest = kwargs["type"]
        # print(typeOfRequest)
        if typeOfRequest == "medical":
            natureOfQuery = constants.NatureOfQuery.MEDICAL.value
            student_list = ApplicationStatus.objects.filter(campus = campus,
                natureOfQuery = natureOfQuery).order_by('-lastChangedDate')
        elif typeOfRequest == "informative":
            return self.getInformativeQueryList(request)
        else:
            if typeOfRequest == "pending":
                level = 1
            elif typeOfRequest == "forwarded":
                level = 2

            if user_profile_object.token == constants.UserType.CMO.value:
                student_list = ApplicationStatus.objects.filter(campus = campus, level = level, 
                natureOfQuery = constants.NatureOfQuery.MEDICAL.value, attempt=1).order_by('-lastChangedDate')
            else:
                student_list = ApplicationStatus.objects.filter(Q(natureOfQuery = constants.NatureOfQuery.NONMEDICAL.value) | Q(natureOfQuery = constants.NatureOfQuery.NOTALLOTED.value),
                    campus = campus, level = level, attempt=1).order_by('-lastChangedDate')
        
        returnList=[]
        for student in student_list:
            dict1 = {
                "id":student.student_id.user.username,
                "name":student.student_id.name,
                "description":student.description,
                "status" : constants.Status(student.status).name,
                "level" : student.level,
                "attempt" : student.attempt,
                "date": str(student.lastChangedDate.date()) + " " + str(student.lastChangedDate.time())[0:8],
                "natureOfQuery": student.natureOfQuery,
            }
            returnList.append(dict1) 
        return JsonResponse(returnList, safe=False)

    def getInformativeQueryList(self, request):
        user_object = request.user
        user_profile_object = UserProfile.objects.get(user_id=user_object)
        campus = user_profile_object.campus
        if user_profile_object.token == constants.UserType.DEAN.value:
            student_list = InformativeQueryForm.objects.order_by('-lastChangedDate')
        else:
            student_list = InformativeQueryForm.objects.filter(campus=campus).order_by('-lastChangedDate')
        return_list = []
        for student in student_list:
            dict1 = {
                "id": student.student_id.user.username,
                "name": student.student_id.name,
                "status": constants.Status(student.status).name,
                "attempt": student.attempt,
                "date": str(student.lastChangedDate.date()) + " " + str(student.lastChangedDate.time())[0:8],
            }
            return_list.append(dict1)
        return JsonResponse(return_list, safe=False)

    def getPSDStudentList(self, request, typeOfRequest):
        user_object = request.user
        user_profile_object = UserProfile.objects.get(user_id = user_object)
        # campus =  user_profile_object.campus  ## Uncomment for seperating list on campus basis. Also add filter below
        # typeOfRequest = request.POST.get['type']
        student_list = []
        if typeOfRequest == "pending":
            student_list = InformativeQueryForm.objects.filter(status = 1,).order_by('-lastChangedDate')
        elif typeOfRequest == "forwarded":
            student_list = InformativeQueryForm.objects.exclude(status = 1).order_by('-lastChangedDate')

        returnList=[]
        for student in student_list:
            dict1 = {
                "id":student.student_id.user.username,
                "name":student.student_id.name,
                "status" : constants.Status(student.status).name,
                "attempt" : student.attempt,
                "date": str(student.lastChangedDate.date()) + " " + str(student.lastChangedDate.time())[0:8],
            }
            returnList.append(dict1)
        # print(returnList)
        return JsonResponse(returnList, safe=False)

    def getDEANStudentList(self, request, typeOfRequest):
        user_object = request.user
        user_profile_object = UserProfile.objects.get(user_id=user_object)
        if typeOfRequest == "medical":
            natureOfQuery = constants.NatureOfQuery.MEDICAL.value
            student_list = ApplicationStatus.objects.filter(
                natureOfQuery = natureOfQuery).order_by('-lastChangedDate')
        elif typeOfRequest == "informative":
            return self.getInformativeQueryList(request)
        else:
            if typeOfRequest == "pending":
                level = 1
            elif typeOfRequest == "forwarded":
                level = 2

            if user_profile_object.token == constants.UserType.CMO.value:
                student_list = ApplicationStatus.objects.filter(level = level, 
                natureOfQuery = constants.NatureOfQuery.MEDICAL.value, attempt=1).order_by('-lastChangedDate')
            else:
                student_list = ApplicationStatus.objects.filter(Q(natureOfQuery = constants.NatureOfQuery.NONMEDICAL.value) | Q(natureOfQuery = constants.NatureOfQuery.NOTALLOTED.value), level = level, attempt=1).order_by('-lastChangedDate')
            
        
        returnList=[]
        for student in student_list:
            dict1 = {
                "id":student.student_id.user.username,
                "name":student.student_id.name,
                "description":student.description,
                "status" : constants.Status(student.status).name,
                "level" : student.level,
                "attempt" : student.attempt,
                "date": str(student.lastChangedDate.date()) + " " + str(student.lastChangedDate.time())[0:8],
            }
            returnList.append(dict1) 
        return JsonResponse(returnList, safe=False)
@method_decorator([login_required, level1_required], name='dispatch')
class level1StudentView(generic.View):
    def get(self, request, *args, **kwargs):
        student_id = kwargs['student_id']
        userProfile_object = UserProfile.objects.get(user=User.objects.get(username = student_id))
            
        #PSD PAGE
        if UserProfile.objects.get(user = request.user).token == constants.UserType.PSD.value:
            params = viewOnlyPSDStudentPageView.getStudentDetail(student_id)
            return render(request, "grievance/psdStudentPage.html", params)

        #Dean Page
        if UserProfile.objects.get(user = request.user).token == constants.UserType.DEAN.value:
            params = viewOnlyStudentPageView.getStudentDetail(student_id)
            return render(request, "grievance/viewOnlyStudentPage.html", params)

        #Other users
        ApplicationStatus_object = ApplicationStatus.objects.get(student_id = userProfile_object,attempt =1)
        grievanceForm_object = GrievanceForm.objects.get(student_id = userProfile_object)
        documents = self.getDocuments(grievanceForm_object)
        if documents:
            documentCount = len(documents)
        else:
            documentCount = 0
        params={
            'name' : userProfile_object.name,
            'student_id' : student_id,
            'allocatedStation' : grievanceForm_object.allocatedStation,
            'applicationDate' : ApplicationStatus_object.lastChangedDate,
            'description': ApplicationStatus_object.description,
            'documentCount': documentCount,
            'documents': documents,
            'cg': userProfile_object.cg,
            'back': "/CMS/level1/",
        }
        return render(request,"grievance/cmoAndADStudentPage.html",params)

    def post(self, request, *args, **kwargs):
        if UserProfile.objects.get(user = request.user).token == constants.UserType.PSD.value:
            # print(request.POST)
            student_id = kwargs['student_id']
            userProfile_object = UserProfile.objects.get(user=User.objects.get(username = student_id))
            attempt = request.POST.get('attempt')
            level1comment = request.POST.get('reply')

            informativeQuerryForm_object = InformativeQueryForm.objects.get(student_id = userProfile_object, attempt = attempt)

            informativeQuerryForm_object.level1Comment = level1comment
            informativeQuerryForm_object.status = constants.Status.APPROVED.value

            informativeQuerryForm_object.save()

        else:
            student_id = kwargs['student_id']
            userProfile_object = UserProfile.objects.get(user=User.objects.get(username = student_id))
            ApplicationStatus_object = ApplicationStatus.objects.get(student_id = userProfile_object, attempt =1)
            grievanceForm_object = GrievanceForm.objects.get(student_id = userProfile_object)

            priority = request.POST.get("priority")
            level1comment = request.POST.get("remarks")

            grievanceForm_object.priority = priority

            ApplicationStatus_object.level1Comment = level1comment
            ApplicationStatus_object.level = 2
            ApplicationStatus_object.status = constants.Status.PENDING.value
            ApplicationStatus_object.lastChangedDate = datetime.now()

            ApplicationStatus_object.save()
            grievanceForm_object.save()

        return HttpResponseRedirect('/CMS/redirect/')


    def getDocuments(self, grievanceForm_object):
        documents = []
        documentCount = 0
        if grievanceForm_object.document1:
            documentCount+=1
            documents.append(grievanceForm_object.document1)
        if grievanceForm_object.document2:
            documentCount+=1
            documents.append(grievanceForm_object.document2)
        if grievanceForm_object.document3:
            documentCount+=1
            documents.append(grievanceForm_object.document3)
        if grievanceForm_object.document4:
            documentCount+=1
            documents.append(grievanceForm_object.document4)
        if grievanceForm_object.document5:
            documentCount+=1
            documents.append(grievanceForm_object.document5)
        return documents

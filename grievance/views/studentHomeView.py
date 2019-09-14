from grievance.models import ApplicationStatus,GrievanceForm, UserProfile
from django.shortcuts import render
from grievance.forms import StudentHomeViewForm, ApplicationStatusForm
import datetime
from . import constants as constants
from django.views import generic

class studenthomeview():
    def get(self, request,*args, **kwargs):
        current_user=request.user
        user = UserProfile.objects.get(user=current_user)
        formEntry = GrievanceForm.objects.get(student_id = user)
        const= constants.Status.NOAPPLICATION.value()
        attempt_status=[const,const,const]
        description=["","",""]
        comments=["","",""]
        newStation=["","",""]
        if formEntry:
            i=0
            applicationstatus_list = ApplicationStatus.objects.filter(student_id = user)
            for x in applicationstatus_list:
                attempt_status[x.attempt-1]=x.status
                comments[x.attempt-1]=x.level2Comment
                newStation[x.attempt-1]=x.newStation
                i+=1
            details={       #things to be passed to front end
            'formEntry':formEntry,
            'attemptStatus':attempt_status,
            'description'
            'campus':user.campus,
            'name': user.name,
            'comments':comments,
            'newStation':newStation
            }
            #TODO : return render
        else:
            attempt_status = [const,const,const]
            #TODO : return render while sending only the attempt status
    def post(self, request, *args, **kwargs):
        current_user=request.user
        user = UserProfile.objects.get(user=current_user)
        if request.POST.get("Application1"):
            formEntry = GrievanceForm.objects.get(student_id=user)
            if not formEntry:
                formEntry = GrievanceForm.create(student_id=user)
                applicationStatus = ApplicationStatus.create(student_id = user)
                form1 = StudentHomeViewForm(request.POST, request.FILES, instance=formEntry)
                form2 = ApplicationStatusForm(request.POST, instance = applicationStatus)
                form1.save()
                form2.save()
                formEntry.applicationDate = datetime.datetime.now()
                formEntry.priority = constants.priority.LOW.value()
                applicationStatus.status = constants.Status.INPROGRESS.value()
                applicationStatus.attempt = constants.Attempt.ATTEMPT1.value()
                applicationStatus.level = constants.Levels.LEVEL1.value()
                applicationStatus.lastChangedDate = formEntry.applicationDate
                applicationStatus.campus = user.campus
                applicationStatus.natureOfQuery = formEntry.natureOfQuery
                #return render
            else:
                #redirect
                print("")
        elif request.POST.get("Application2"):
            formEntry = GrievanceForm.get(user = current_user)
            applicationStatus = ApplicationStatus.objects.get(student_id=user)
            if(formEntry.attempt==1):
                form1 = StudentHomeViewForm(request.POST, request.FILES, instance=formEntry)
                form2 = ApplicationStatusForm(request.POST, instance = applicationStatus)
                form1.save()
                form2.save()
                formEntry.attempt = constants.Attempt.ATTEMPT2.value()
                applicationStatus.level = constants.Levels.LEVEL2.value()                
                applicationStatus.lastChangedDate = formEntry.applicationDate
                #return render
            else:   
                #redirect
                print("") 
        elif request.POST.get("Application3"):
           formEntry = GrievanceForm.get(user = current_user)
           applicationStatus = ApplicationStatus.objects.get(student_id=user)
           if(formEntry.attempt==2):
               form1 = StudentHomeViewForm(request.POST, request.FILES, instance=formEntry)
               form2 = ApplicationStatusForm(request.POST, instance = applicationStatus)
               form1.save()
               form2.save()
               formEntry.attempt = constants.Attempt.ATTEMPT3.value()
               applicationStatus.level = constants.Levels.LEVEL2.value()                
               applicationStatus.lastChangedDate = formEntry.applicationDate

               #return render


                





         


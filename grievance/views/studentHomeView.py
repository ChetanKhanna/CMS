from grievance.models import ApplicationStatus,GrievanceForm, UserProfile, User
from django.shortcuts import render
from grievance.forms import StudentHomeViewForm, ApplicationStatusForm
import datetime
from . import constants as constants
from django.views import generic

class studenthomeview(generic.TemplateView):
    def get(self, request,*args, **kwargs):
        # current_user=request.user
        # user = UserProfile.objects.get(user=current_user)
        user = UserProfile.objects.get(user=User.objects.get(username="20160080G"))
        # const= str(constants.Status.NOAPPLICATION.value())
        const = "0"
        attempt_status=[const,const,const]
        description=["","",""]
        comments=["","",""]
        newStation=["","",""]
        if (GrievanceForm.objects.filter(student_id = user).count())!=0:
            formEntry = GrievanceForm.objects.get(student_id = user)
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
            'descriptions' : description,
            'campus':user.campus,
            'name': user.name,
            'comments':comments,
            'newStation':newStation
            }
            return render (request, "grievance/grievanceForm.html", details)
            #TODO : return render
        else:
            attempt_status = [const,const,const]
            return render (request, "grievance/grievanceForm.html", {'attemptStatus':attempt_status,'name':user.name,'campus':user.campus,'descriptions':description,'comments':comments,
            'newStation':newStation})

    def post(self, request, *args, **kwargs):
        # current_user=request.user
        # user = UserProfile.objects.get(user=current_user)
        user = UserProfile.objects.get(user=User.objects.get(username="20160080G"))
        if request.POST.get("submit1"):
            if (GrievanceForm.objects.filter(student_id = user).count())==0:
                # formEntry = GrievanceForm.objects.create(student_id=user)
                # applicationStatus = ApplicationStatus.objects.create(student_id = user)
                temp = StudentHomeViewForm(request.POST, request.FILES)
                temp2 = ApplicationStatusForm(request.POST)
                form1=temp.save(commit=False)
                form2=temp2.save(commit=False)
                form1.student_id=user
                form2.student_id=user
                form1.applicationDate = datetime.datetime.now()
                form1.priority = 1#constants.priority.LOW.value()
                form1.save()
                form2.status = 1#constants.Status.INPROGRESS.value()
                form2.attempt = 1
                form2.level = 1
                form2.lastChangedDate = datetime.datetime.now()
                form2.campus = user.campus
                form2.natureOfQuery = form1.natureOfQuery
                form2.save()
                #return render
            else:
                #redirect
                print("")
        elif request.POST.get("submit2"):
            # formEntry = GrievanceForm.objects.get(user = user)
            # applicationStatus = ApplicationStatus.objects.get(student_id = user)
            # formEntry = GrievanceForm.objects.get(user = user)
            applicationStatus = ApplicationStatus.objects.get(student_id = user)
            if(applicationStatus.attempt==1):
                applicationStatus.attempt = 2
                applicationStatus.level = 2           
                applicationStatus.status = 1     
                applicationStatus.lastChangedDate = datetime.datetime.now()
                form2 = ApplicationStatusForm(request.POST, instance = applicationStatus)
                form2.save() 
                #return render
            else:   
                #redirect
                print("") 
        elif request.POST.get("submit3"):
           # formEntry = GrievanceForm.objects.get(user = user)
           # applicationStatus = ApplicationStatus.objects.get(student_id = user)
        #    formEntry = GrievanceForm.get(user = user)
           applicationStatus = ApplicationStatus.objects.get(student_id = user)
           if(applicationStatus.attempt==2):
               applicationStatus.attempt = 3
               applicationStatus.level = 2
               applicationStatus.status = 1                
               applicationStatus.lastChangedDate = datetime.datetime.now()
               form2 = ApplicationStatusForm(request.POST, instance = applicationStatus)
               form2.save()
               #return render


                





         


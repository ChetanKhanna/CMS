from grievance.models import ApplicationStatus,GrievanceForm, UserProfile, User
from django.shortcuts import render
from grievance.forms import StudentHomeViewForm, ApplicationStatusForm
import datetime
from . import constants as constants
from django.views import generic
from django.http import HttpResponseRedirect

class studentHomeView(generic.TemplateView):

    def redirect(self):
        return HttpResponseRedirect('/ps-grievance/redirect')

    def get(self, request,*args, **kwargs):
        current_user=request.user
        user = UserProfile.objects.get(user=current_user)
        const = constants.Status.NOAPPLICATION.value
        attempt_status=[const,const,const]
        description=["","",""]
        comments=["","",""]
        newStation=["","",""]

        # formEntry = GrievanceForm.objects.get(student_id = user)
        applicationstatus_list = ApplicationStatus.objects.filter(student_id = user)
        for x in applicationstatus_list:
            attempt_status[x.attempt-1]=x.status-1
            comments[x.attempt-1]=x.level2Comment
            newStation[x.attempt-1]=x.newStation
            description[x.attempt-1]=x.description

        details={       #things to be passed to front end
        'attemptStatus':attempt_status,
        'descriptions' : description,
        'campus':user.campus,
        'name': user.name,
        'comments':comments,
        'newStation':newStation
        }
        return render (request, "grievance/grievanceForm.html", details)
       
    def post(self, request, *args, **kwargs):
        current_user=request.user
        user = UserProfile.objects.get(user=current_user)
        if request.POST.get("submit1"):
            print("\n\n-----------------asdf----------------")
            print(request.POST)
            if (GrievanceForm.objects.filter(student_id = user).count())==0:
                temp1 = StudentHomeViewForm(request.POST, request.FILES)
                form1 = temp1.save(commit=False)
                form2 = ApplicationStatusForm(request.POST).save(commit=False)
                form1.student_id=user
                form1.applicationDate = datetime.datetime.now()
                form1.priority = constants.Priority.LOW.value
                form1.save()
                form2.student_id=user
                form2.status = constants.Status.INPROGRESS.value
                form2.attempt = 1
                form2.level = 1
                form2.lastChangedDate = datetime.datetime.now()
                form2.campus = user.campus
                form2.natureOfQuery = form1.natureOfQuery
                form2.save()
                return self.redirect()
            else:
                return self.redirect()
        elif request.POST.get("submit2"):
            # formEntry = GrievanceForm.objects.get(user = user)
            # applicationStatus = ApplicationStatus.objects.get(student_id = user)
            # formEntry = GrievanceForm.objects.get(user = user)
            applicationStatus_object = ApplicationStatus.objects.filter(student_id = user)
            if(len(applicationStatus_object) == 1):
                form = ApplicationStatusForm(request.POST).save(commit=False)
                form.student_id = user
                form.status = constants.Status.INPROGRESS.value
                form.attempt = 2
                form.level = 2
                form.lastChangedDate = datetime.datetime.now()
                form.campus = user.campus
                form.natureOfQuery = applicationStatus_object[0].natureOfQuery
                form.save()
                return self.redirect()
            else:   
                return self.redirect() 
        elif request.POST.get("submit3"):
           # formEntry = GrievanceForm.objects.get(user = user)
           # applicationStatus = ApplicationStatus.objects.get(student_id = user)
        #    formEntry = GrievanceForm.get(user = user)
            applicationStatus_object = ApplicationStatus.objects.filter(student_id = user)
            if(len(applicationStatus_object) == 2):
                form = ApplicationStatusForm(request.POST).save(commit=False)
                form.student_id = user
                form.status = constants.Status.INPROGRESS.value
                form.attempt = 3
                form.level = 2
                form.lastChangedDate = datetime.datetime.now()
                form.campus = user.campus
                form.natureOfQuery = applicationStatus_object[0].natureOfQuery
                form.save()
                return self.redirect()
            else:   
                return self.redirect() 

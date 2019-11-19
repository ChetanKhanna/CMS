from grievance.models import (ApplicationStatus, GrievanceForm,
                              UserProfile, User, InformativeQueryForm)
from django.shortcuts import render
from grievance.forms import StudentHomeViewForm, ApplicationStatusForm
from django.utils import timezone as datetime
from . import constants as constants
from django.views import generic
from django.http import HttpResponseRedirect

#import decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from grievance.customDecorator import student_required

#import deadline
from grievance.views import deadlineView

@method_decorator([login_required, student_required], name='dispatch')
class studentHomeView(generic.TemplateView):

    def redirect(self):
        return HttpResponseRedirect('/PS2/redirect')

    def getDetails(self, current_user):
        user = UserProfile.objects.get(user=current_user)
        const = constants.Status.NOAPPLICATION.value
        # Non Informative Queries
        attempt_status=[const,const,const]
        description=["","",""]
        comments=["","",""]
        newStation=["","",""]
        formEntry = None
        if len(GrievanceForm.objects.filter(student_id=user)) ==1:
            formEntry = GrievanceForm.objects.get(student_id = user)
        applicationstatus_list = ApplicationStatus.objects.filter(student_id = user)
        for x in applicationstatus_list:
            status = x.status
            # if not published by the team, then pending status must be displayed
            if(status == constants.Status.APPROVED.value or status == constants.Status.REJECTED.value) and x.publish == 0 :
                status = constants.Status.PENDING.value
            attempt_status[x.attempt-1]=status
            comments[x.attempt-1]=x.level2Comment
            newStation[x.attempt-1]=x.newStation
            description[x.attempt-1]=x.description
        # Informative Queries
        informativeQueryStatuses = [const, const, const]
        informativeQueryDescriptions = ["", "", ""]
        informativeQueryComments = ["", "", ""]
        informativeQueryAllocatedStation = ""
        informativeQueryPreferenceNumberOfAllocatedStation = 0
        informativeQuery_list = InformativeQueryForm.objects.filter(student_id=user)
        for x in informativeQuery_list:
            informativeQueryStatuses[x.attempt-1] = x.status
            informativeQueryDescriptions[x.attempt-1] = x.description
            informativeQueryComments[x.attempt-1] = x.level1Comment
            if x.attempt == 1:
                informativeQueryAllocatedStation = x.allocatedStation
                informativeQueryPreferenceNumberOfAllocatedStation = x.preferenceNumberOfAllocatedStation

        details={       #things to be passed to front end
        'formEntry' : formEntry,
        'attemptStatus':attempt_status,
        'descriptions' : description,
        'campus':user.campus,
        'name': user.name,
        'cg': user.cg,
        'id': user.user.username,
        'email': user.email,
        'comments':comments,
        'newStation':newStation,
        'informativeQueryStatuses': informativeQueryStatuses,
        'informativeQueryDescriptions': informativeQueryDescriptions,
        'informativeQueryComments': informativeQueryComments,
        'informativeQueryAllocatedStation' : informativeQueryAllocatedStation,
        'informativeQueryPreferenceNumberOfAllocatedStation' : informativeQueryPreferenceNumberOfAllocatedStation,
        'back': "/PS2/login/",
        'expired' : deadlineView.checkAllDeadline(),
        'deadlines' : deadlineView.getDeadlines(),
        }

        return details


    def get(self, request, *args, **kwargs):
        current_user=request.user
        details = self.getDetails(current_user)
        return render (request, "grievance/studentHomePage.html", details)
       
    def post(self, request, *args, **kwargs):
        current_user=request.user
        user = UserProfile.objects.get(user=current_user)
        # Non Informative Queries
        if request.POST.get("submit1"):
            if (GrievanceForm.objects.filter(student_id = user).count())==0 and deadlineView.checkDeadline(1) == 0:
                form1 = StudentHomeViewForm(request.POST, request.FILES).save(commit=False)
                form2 = ApplicationStatusForm(request.POST).save(commit=False)
                form1.student_id=user
                form1.campus = user.campus
                form1.applicationDate = datetime.now()
                form1.priority = 0
                form1.save()
                form2.student_id=user
                form2.status = constants.Status.INPROGRESS.value
                form2.attempt = 1
                form2.level = 1
                form2.campus = user.campus
                form2.natureOfQuery = form1.natureOfQuery
                form2.save()
                return self.redirect()
            else:
                return self.redirect()
        elif request.POST.get("submit2"):
            applicationStatus_object = ApplicationStatus.objects.filter(student_id = user)
            if(len(applicationStatus_object) == 1)  and deadlineView.checkDeadline(2) == 0:
                form = ApplicationStatusForm(request.POST).save(commit=False)
                form.student_id = user
                form.status = constants.Status.INPROGRESS.value
                form.attempt = 2
                form.level = 2
                form.lastChangedDate = datetime.now()
                form.campus = user.campus
                form.natureOfQuery = applicationStatus_object[0].natureOfQuery
                form.save()
                return self.redirect()
            else:   
                return self.redirect() 
        elif request.POST.get("submit3"):
            applicationStatus_object = ApplicationStatus.objects.filter(student_id = user)
            if(len(applicationStatus_object) == 2)  and deadlineView.checkDeadline(3) == 0:
                form = ApplicationStatusForm(request.POST).save(commit=False)
                form.student_id = user
                form.status = constants.Status.INPROGRESS.value
                form.attempt = 3
                form.level = 2
                form.lastChangedDate = datetime.now()
                form.campus = user.campus
                form.natureOfQuery = applicationStatus_object[0].natureOfQuery
                form.save()
                return self.redirect()
            else:   
                return self.redirect()
        # Informative Queries
        elif request.POST.get('informativeQuery1Submit') and not \
            InformativeQueryForm.objects.filter(student_id=user, attempt=1):
            InformativeQueryForm.objects.create(student_id=user, attempt=1, status=1,
                description=request.POST.get('description'), campus=user.campus, 
                allocatedStation = request.POST.get('informativeQueryAllocatedStation'),
                preferenceNumberOfAllocatedStation = request.POST.get('informativeQueryPreferenceNumberOfAllocatedStation'))
            return HttpResponseRedirect('/PS2/redirect')
        elif request.POST.get('informativeQuery2Submit') and not \
            InformativeQueryForm.objects.filter(student_id=user, attempt=2):
            InformativeQueryForm.objects.create(student_id=user, attempt=2, status=1,
                description=request.POST.get('description'), campus=user.campus)
            return HttpResponseRedirect('/PS2/redirect')
        elif request.POST.get('informativeQuery3Submit') and not \
            InformativeQueryForm.objects.filter(student_id=user, attempt=3):
            InformativeQueryForm.objects.create(student_id=user, attempt=3, status=1,
                description=request.POST.get('description'), campus=user.campus)
            return HttpResponseRedirect('/PS2/redirect')
        else:
            return HttpResponseRedirect('/PS2/redirect')


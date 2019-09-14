from django import forms
from .models import GrievanceForm, UserProfile, ApplicationStatus

class StudentHomeViewForm(forms.ModelForm):
    class Meta:
        model = GrievanceForm
        fields = ('document1','document2','document3','document4','document5','preferedStation1','preferedStation2','preferedStation3','preferedStation4',
                    'preferedStation5','preferenceNumberOfAllocatedStation','allocatedStation','offShoot','cg','natureOfQuery')

class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = ApplicationStatus
        fields = ('description') 
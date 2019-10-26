from django import forms
from .models import GrievanceForm, ApplicationStatus, InformativeQueryForm


class StudentHomeViewForm(forms.ModelForm):
    class Meta:
        model = GrievanceForm
        fields = ('document1', 'document2', 'document3', 'document4', 'document5', 'preferedStation1',
        		  'preferedStation2', 'preferedStation3', 'preferedStation4', 'preferedStation5',
                  'preferedStation6', 'preferedStation7', 'preferedStation8', 'preferedStation9',
                  'preferedStation10', 'allocatedStation', 'natureOfQuery')


class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = ApplicationStatus
        fields = ('description',)


class InformativeQuery(forms.ModelForm):
	class Meta:
		model = InformativeQueryForm
		fields = ('status', 'description', 'level1Comment',)

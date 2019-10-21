from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class UserProfileAdmin(admin.ModelAdmin):

    model = UserProfile
    list_display = ('user','name','token','contact','email','campus','cg',)
    list_filter = ('campus',)
    search_fields = ('user__username','name')
    ordering = ()
    filter_horizontal = ()
    fieldsets = ()

class ApplicationStatusAdmin(admin.ModelAdmin):
    
    model = ApplicationStatus
    list_display = ('student_id','attempt', 'campus', 'level', 'status', 'natureOfQuery', 'publish',)
    list_filter = ('attempt',)
    search_fields = ('student_id__user__username','attempt',)
    ordering = ()
    filter_horizontal = ()
    fieldsets = ()

class GrievanceFormAdmin(admin.ModelAdmin):
    
    model = GrievanceForm
    list_display = ('student_id', 'campus', 'natureOfQuery',)
    list_filter = ('student_id__name',)
    search_fields = ('student_id__name',)
    ordering = ()
    filter_horizontal = ()
    fieldsets = ()

class DeadlineAdmin(admin.ModelAdmin):
    
    model = GrievanceForm
    list_display = ('attempt', 'date',)
    list_filter = ()
    search_fields = ()
    ordering = ()
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(GrievanceForm, GrievanceFormAdmin)
admin.site.register(ApplicationStatus, ApplicationStatusAdmin)
admin.site.register(InformativeQuerryForm)
admin.site.register(Deadline, DeadlineAdmin)
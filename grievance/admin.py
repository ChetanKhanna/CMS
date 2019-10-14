from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from grievance.models import UserProfile, ApplicationStatus, GrievanceForm
# Register your models here.
from .models import *


class UserProfileAdmin(UserAdmin):

    model = UserProfile
    # list_display = ('user','token','name','contact','email','campus','cg')
    # search_fields = ('name','contact','email','campus')
    list_display = ('name',)
    list_filter = ()
    search_fields = ('name',)
    ordering = ()
    filter_horizontal = ()
    fieldsets = ()

class ApplicationStatusAdmin(UserAdmin):
    
    model = ApplicationStatus
    # list_display = ('user','token','name','contact','email','campus','cg')
    # search_fields = ('name','contact','email','campus')
    list_display = ('student_id',)
    list_filter = ('student_id__name',)
    search_fields = ('student_id__name',)
    ordering = ()
    filter_horizontal = ()
    fieldsets = ()

class GrievanceFormAdmin(UserAdmin):
    
    model = GrievanceForm
    # list_display = ('user','token','name','contact','email','campus','cg')
    # search_fields = ('name','contact','email','campus')
    list_display = ('student_id',)
    list_filter = ()
    search_fields = ('student_id__name',)
    ordering = ()
    filter_horizontal = ()
    fieldsets = ()


admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(Student)
# admin.site.register(OtherUsers)
admin.site.register(GrievanceForm, GrievanceFormAdmin)
admin.site.register(ApplicationStatus, ApplicationStatusAdmin)
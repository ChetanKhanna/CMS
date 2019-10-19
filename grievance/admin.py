from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from grievance.models import UserProfile, ApplicationStatus, GrievanceForm
# Register your models here.
from .models import *


# class UserProfileAdmin(UserAdmin):

#     model = UserProfile
#     # list_display = ('user','token','name','contact','email','campus','cg')
#     # search_fields = ('name','contact','email','campus')
#     list_display = ('user','name','token','contact','email','campus','cg',)
#     list_filter = ('campus',)
#     search_fields = ('name',)
#     ordering = ()
#     filter_horizontal = ()
#     fieldsets = ()

# class ApplicationStatusAdmin(UserAdmin):
    
#     # model = ApplicationStatus
#     # list_display = ('user','token','name','contact','email','campus','cg')
#     # search_fields = ('name','contact','email','campus')
#     list_display = ('student_id','attempt',)
#     list_filter = ('attempt',)
#     search_fields = ('student_id__user__username','attempt',)
#     ordering = ()
#     filter_horizontal = ()
#     fieldsets = ()

# class GrievanceFormAdmin(UserAdmin):
    
#     # model = GrievanceForm
#     # list_display = ('user','token','name','contact','email','campus','cg')
#     # search_fields = ('name','contact','email','campus')
#     list_display = ('student_id',)
#     list_filter = ('student_id__name',)
#     search_fields = ('contact',)
#     # raw_id_fields = ('student_id',)
#     # autocomplete_fields=['student_id',]
#     ordering = ()
#     filter_horizontal = ()
#     fieldsets = ()


admin.site.register(UserProfile)
# admin.site.register(Student)
# admin.site.register(OtherUsers)
admin.site.register(GrievanceForm)
admin.site.register(ApplicationStatus)
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .models import *
from import_export.admin import ImportExportModelAdmin

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        
class UserAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = UserResource
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    import_id_fields = ('username', 'first_name', 'last_name', 'email')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields =('user','token','name','contact','email','campus','cg',)


class UserProfileAdmin(ImportExportModelAdmin):

    resource_class = UserProfileResource
    list_display = ('user','name','token','contact','email','campus','cg',)
    list_filter = ('campus',)
    search_fields = ('user__username','name')
    ordering = ()
    filter_horizontal = ()
    fieldsets = ()
    

admin.site.register(UserProfile, UserProfileAdmin)

    

class ApplicationStatusAdmin(ImportExportModelAdmin):
    
    model = ApplicationStatus
    list_display = ('student_id','attempt', 'campus', 'level', 'status', 'natureOfQuery', 'publish', 'lastChangedDate',)
    list_filter = ('attempt',)
    search_fields = ('student_id__user__username','attempt',)
    ordering = ()
    filter_horizontal = ()
    fieldsets = ()

class GrievanceFormAdmin(ImportExportModelAdmin):
    
    model = GrievanceForm
    list_display = ('student_id', 'campus', 'natureOfQuery',)
    list_filter = ('student_id__name',)
    search_fields = ('student_id__name',)
    ordering = ()
    filter_horizontal = ()
    fieldsets = ()

class DeadlineAdmin(ImportExportModelAdmin):
    
    model = GrievanceForm
    list_display = ('attempt', 'date',)
    list_filter = ()
    search_fields = ()
    ordering = ()
    filter_horizontal = ()
    fieldsets = ()


admin.site.register(GrievanceForm, GrievanceFormAdmin)
admin.site.register(ApplicationStatus, ApplicationStatusAdmin)
admin.site.register(InformativeQueryForm)
admin.site.register(Deadline, DeadlineAdmin)

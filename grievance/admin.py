from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(UserType)
admin.site.register(Student)
admin.site.register(OtherUsers)
admin.site.register(GrievanceForm)
admin.site.register(ApplicationStatus)
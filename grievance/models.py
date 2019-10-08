from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
import os


def validate_document(document):
    file_size = document.file.size
    # limit_kb = 150
    # if file_size > limit_kb * 1024:
    #     raise ValidationError("Max size of file is %s KB" % limit)

    limit_mb = 5
    if file_size > limit_mb * 1024 * 1024:
       raise ValidationError("Max size of file is %s MB" % limit_mb)

def path_and_rename(instance, filename):
    upload_to = 'documents/' + str(instance.student_id)
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(instance.student_id, get_random_string(), ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


# Create your models here.

# class UserType(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	token = models.IntegerField(default=0)

class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
	# token to know the type of user
	token = models.IntegerField(default=0)
	# user profile related data
	name = models.CharField(max_length = 100)
	contact = models.CharField(max_length = 20)
	email = models.EmailField()
	campus = models.IntegerField(default = 0)
	cg = models.CharField(max_length = 10)

	def __str__(self):
		return str(self.user)

class GrievanceForm(models.Model):
	student_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, primary_key=True)
	contactNumber = models.CharField(max_length = 15)
	allocatedStation = models.CharField(max_length = 500)
	preferenceNumberOfAllocatedStation = models.IntegerField()
	natureOfQuery = models.IntegerField()
	applicationDate = models.DateTimeField()
	preferedStation1 = models.CharField(max_length = 500)
	preferedStation2 = models.CharField(max_length = 500, blank=True)
	preferedStation3 = models.CharField(max_length = 500, blank=True)
	preferedStation4 = models.CharField(max_length = 500, blank=True)
	preferedStation5 = models.CharField(max_length = 500, blank=True)
	preferedStation6 = models.CharField(max_length = 500, blank=True)
	preferedStation7 = models.CharField(max_length = 500, blank=True)
	preferedStation8 = models.CharField(max_length = 500, blank=True)
	preferedStation9 = models.CharField(max_length = 500, blank=True)
	preferedStation10 = models.CharField(max_length = 500, blank=True)
	document1 = models.FileField(upload_to=path_and_rename,validators=[FileExtensionValidator(allowed_extensions=['pdf']),validate_document], blank=True)
	document2 = models.FileField(upload_to=path_and_rename,validators=[FileExtensionValidator(allowed_extensions=['pdf']),validate_document], blank=True)
	document3 = models.FileField(upload_to=path_and_rename,validators=[FileExtensionValidator(allowed_extensions=['pdf']),validate_document], blank=True)
	document4 = models.FileField(upload_to=path_and_rename,validators=[FileExtensionValidator(allowed_extensions=['pdf']),validate_document], blank=True)
	document5 = models.FileField(upload_to=path_and_rename,validators=[FileExtensionValidator(allowed_extensions=['pdf']),validate_document], blank=True)
	priority = models.IntegerField(blank=True)

	def __str__(self):
		return str(self.student_id)

class ApplicationStatus(models.Model):
	student_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	attempt = models.IntegerField()
	level = models.IntegerField()
	status = models.IntegerField()
	lastChangedDate = models.DateTimeField(auto_now_add=True)
	description = models.CharField(max_length = 500)
	level1Comment = models.CharField(max_length = 500, blank=True)
	level2Comment = models.CharField(max_length = 500, blank=True)
	newStation = models.CharField(max_length = 500, blank=True)
	campus = models.IntegerField(default = 0)
	natureOfQuery = models.IntegerField(default = 0)
	publish = models.IntegerField(default=0)
	
	class Meta:
		unique_together = (('student_id', 'attempt'),)

	def __str__(self):
		return str((self.student_id,self.attempt))
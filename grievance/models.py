from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class UserType(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	token = models.IntegerField(default=0)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	# token to know the type of user
	token = models.IntegerField(default=0)
	# user profile related data
	name = models.CharField(max_length = 100)
	contact = models.CharField(max_length = 20)
	email = models.EmailField()
	campus = models.IntegerField(default = 0)

	def __str__(self):
		return str(self.user)

# class OtherUsers(models.Model):
# 	user_id = models.CharField(max_length =25, primary_key=True,unique=True)
# 	name = models.CharField(max_length = 50)
# 	contact = models.CharField(max_length = 20)
# 	email = models.EmailField()
# 	campus = models.IntegerField(default = 0)

# 	def __str__(self):
# 		return str(self.user_id)

class GrievanceForm(models.Model):
	student_id = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
	cg = models.CharField(max_length = 10)
	offShoot = models.CharField(max_length = 10)
	allocatedStation = models.CharField(max_length = 500)
	preferenceNumberOfAllocatedStation = models.IntegerField()
	natureOfQuery = models.IntegerField()
	applicationDate = models.DateTimeField()
	preferedStation1 = models.CharField(max_length = 500)
	preferedStation2 = models.CharField(max_length = 500)
	preferedStation3 = models.CharField(max_length = 500)
	preferedStation4 = models.CharField(max_length = 500)
	preferedStation5 = models.CharField(max_length = 500)
	document1 = models.FileField(upload_to='documents/',)
	document2 = models.FileField(upload_to='documents/',)
	document3 = models.FileField(upload_to='documents/',)
	document4 = models.FileField(upload_to='documents/',)
	document5 = models.FileField(upload_to='documents/',)
	priority = models.IntegerField()

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
	
	class Meta:
		unique_together = (('student_id', 'attempt'),)

	def __str__(self):
		return str((self.student_id,self.attempt))
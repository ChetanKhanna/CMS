from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserType(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	token = models.IntegerField(default=0)

class Student(models.Model):
	student_id = models.CharField(max_length =25, primary_key=True,unique=True)
	name = models.CharField(max_length = 50)
	contact = models.CharField(max_length = 20)
	email = models.EmailField()
	champus = models.CharField(max_length = 10)

	def __str__(self):
		return str(self.student_id)

class GrievanceForm(models.Model):
	student_id = models.OneToOneField(Student, on_delete=models.CASCADE)
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
	priority = models.IntegerField()

	def __str__(self):
		return str(self.student_id)

class ApplicationStatus(models.Model):
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	attempt = models.IntegerField()
	level = models.IntegerField()
	status = models.IntegerField()
	lastChangedDate = models.DateTimeField()
	discription = models.CharField(max_length = 500)
	level1Comment = models.CharField(max_length = 500)
	level2Comment = models.CharField(max_length = 500)
	newStation = models.CharField(max_length = 500)

	class Meta:
		unique_together = (('student_id', 'attempt'),)

	def __str__(self):
		return str((self.student_id,self.attempt))
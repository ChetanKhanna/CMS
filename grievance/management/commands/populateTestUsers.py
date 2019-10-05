from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from grievance.models import *
import datetime

class Command(BaseCommand):
  def _create(self):
    for i in range(10):
      try: 
        (user, created) = User.objects.get_or_create(username="user"+str(i),password="123456")
        (_, _) = UserProfile.objects.get_or_create(user = user, token=0, name="Name "+str(i), contact="9876543210", email="user@mail.com", campus=0)
      except:
        pass
      # user=User.objects.get(username="user"+str(i))
      

    try:
      (user, created) = User.objects.get_or_create(username="cmo",password="123456")
      (_, _) = UserProfile.objects.get_or_create(user = user, token=1, name="CMO "+str(i), contact="9876543210", email="cmo@mail.com", campus=0)
    except:
      pass 
    # user=User.objects.get(username="cmo")
    
    
    try:
      (user, created) = User.objects.get_or_create(username="ad",password="123456")
      (_, _) = UserProfile.objects.get_or_create(user = user, token=2, name="AD ", contact="9876543210", email="ad@mail.com", campus=0)
    except:
      pass
    # user=User.objects.get(username="ad")
    

    for i in range(4):
      user = User.objects.get(username="user"+str(i))
      userProfile = UserProfile.objects.get(user=user)
      GrievanceForm.objects.get_or_create(student_id=userProfile, cg="7.8", offShoot="123", allocatedStation="Cement", preferenceNumberOfAllocatedStation=2, natureOfQuery=1, applicationDate=datetime.datetime.now(), preferedStation1="better cement 1", priority = 0)
      ApplicationStatus.objects.get_or_create(student_id=userProfile, attempt=1,
                                              level=1, status=0, description="Hello",
                                              campus=0, natureOfQuery=0)
      if i%2 == 0:
        ApplicationStatus.objects.get_or_create(student_id=userProfile, attempt=2,
                                              level=1, status=0, description="Hello",
                                              campus=0, natureOfQuery=0)
        if i%3 == 0:
          ApplicationStatus.objects.get_or_create(student_id=userProfile, attempt=3,
                                              level=1, status=0, description="Hello",
                                              campus=0, natureOfQuery=0)

    for i in range(4,8):
      user=User.objects.get(username="user"+str(i))
      userProfile = UserProfile.objects.get(user=user)
      #GrievanceForm.objects.get_or_create(student_id=userProfile, cg="7.8", offShoot="123", allocatedStation="Cement", preferenceNumberOfAllocatedStation=2, natureOfQuery=1, applicationDate=datetime.datetime.now(), preferedStation1="better cement 1", priority = 0)
      # try:
      GrievanceForm.objects.get_or_create(student_id=userProfile, cg="7.8", offShoot="123", allocatedStation="Cement", preferenceNumberOfAllocatedStation=2, natureOfQuery=1, applicationDate=datetime.datetime.now(), preferedStation1="better cement 1", priority = 0)
      # except Exception as e:
        # pass
        # GrievanceForm.objects.get(student_id=userProfile, cg="7.8", offShoot="123", allocatedStation="Cement", preferenceNumberOfAllocatedStation=2, natureOfQuery=1, applicationDate=datetime.datetime.now(), preferedStation1="better cement 1", priority = 0)
      ApplicationStatus.objects.get_or_create(student_id=userProfile, attempt=1,
                                              level=1, status=0, description="Hello",
                                              campus=0, natureOfQuery=0)
      if i%2 == 0:
        ApplicationStatus.objects.get_or_create(student_id=userProfile, attempt=2,
                                              level=1, status=0, description="Hello",
                                              campus=0, natureOfQuery=0)
        if i%3 == 0:
          ApplicationStatus.objects.get_or_create(student_id=userProfile, attempt=3,
                                              level=1, status=0, description="Hello",
                                              campus=0, natureOfQuery=0)



  def handle(self, *args, **options):
    self._create()
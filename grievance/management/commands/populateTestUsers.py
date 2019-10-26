from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from grievance.models import *
import datetime

class Command(BaseCommand):
  def _create(self):
    try:
      (user, created) = User.objects.get_or_create(username="admin", is_superuser=True)
      user.set_password('q')
      user.is_staff = True
      user.is_admin = True
      user.is_superuser = True
      user.save()
    except:
      pass

    for i in range(10):
      try: 
        (user, created) = User.objects.get_or_create(username="2016A7PS008G"+str(i))
        user.set_password('q')
        user.save()
        (_, _) = UserProfile.objects.get_or_create(user = user, token=0, name="Name asdfghjklkjjhghhhfhhfhhfhhfhhfhhfhhfhhfhhfhhfhhfhhfhhfhh"+str(i), contact="9876543210", email="user@mail.com", campus=0, cg=10)
      except:
        pass
      # user=User.objects.get(username="user"+str(i))
      

    try:
      (user, created) = User.objects.get_or_create(username="cmo")
      user.set_password('q')
      user.save()
      (_, _) = UserProfile.objects.get_or_create(user = user, token=1, name="CMO "+str(i), contact="9876543210", email="cmo@mail.com", campus=0, cg=10)
    except:
      pass 
    # user=User.objects.get(username="cmo")
    
    
    try:
      (user, created) = User.objects.get_or_create(username="ad")
      user.set_password('q')
      user.save()
      (_, _) = UserProfile.objects.get_or_create(user = user, token=2, name="AD ", contact="9876543210", email="ad@mail.com", campus=0, cg=10)
    except:
      pass
    # user=User.objects.get(username="ad")

    try:
      (user, created) = User.objects.get_or_create(username="level2")
      user.set_password('q')
      user.save()
      (_, _) = UserProfile.objects.get_or_create(user = user, token=3, name="Allocation team ", contact="9876543210", email="ad@mail.com", campus=0, cg=10)
    except:
      pass

    try:
      (user, created) = User.objects.get_or_create(username="psd")
      user.set_password('q')
      user.save()
      (_, _) = UserProfile.objects.get_or_create(user = user, token=4, name="Allocation team ", contact="9876543210", email="ad@mail.com", campus=0, cg=10)
    except:
      pass
    

    for i in range(4):
      user = User.objects.get(username="2016A7PS008G"+str(i))
      userProfile = UserProfile.objects.get(user=user)
      GrievanceForm.objects.get_or_create(student_id=userProfile, allocatedStation="Cement",
                                          natureOfQuery=1,
                                          applicationDate=datetime.datetime.now(), campus=0,
                                          preferedStation1="better cement 1", priority = 0)

      ApplicationStatus.objects.get_or_create(student_id=userProfile, attempt=1, campus=0,
                                              level=1, status=1, description="Hello",
                                              natureOfQuery=0)
      if i%2 == 0:
        ApplicationStatus.objects.get_or_create(student_id=userProfile, attempt=2, campus=0,
                                              level=2, status=1, description="Hello",
                                              natureOfQuery=0)
        if i%3 == 0:
          # print("\n\n\n\n", i)
          ApplicationStatus.objects.get_or_create(student_id=userProfile, attempt=3, campus=0,
                                              level=2, status=1, description="Hello",
                                              natureOfQuery=0)

    # for i in range(4,8):
    #   user=User.objects.get(username="user"+str(i))
    #   userProfile = UserProfile.objects.get(user=user)
    #   #GrievanceForm.objects.get_or_create(student_id=userProfile, cg="7.8", offShoot="123", allocatedStation="Cement", preferenceNumberOfAllocatedStation=2, natureOfQuery=1, applicationDate=datetime.datetime.now(), preferedStation1="better cement 1", priority = 0)
    #   # try:
    #   GrievanceForm.objects.get_or_create(student_id=userProfile, allocatedStation="Cement", preferenceNumberOfAllocatedStation=2, natureOfQuery=1, applicationDate=datetime.datetime.now(), preferedStation1="better cement 1", priority = 0)
    #   # except Exception as e:
    #     # pass
    #     # GrievanceForm.objects.get(student_id=userProfile, cg="7.8", offShoot="123", allocatedStation="Cement", preferenceNumberOfAllocatedStation=2, natureOfQuery=1, applicationDate=datetime.datetime.now(), preferedStation1="better cement 1", priority = 0)
    #   ApplicationStatus.objects.get_or_create(student_id=userProfile, attempt=1,
    #                                           level=1, status=1, description="Hello",
    #                                           campus=0, natureOfQuery=0)
    #   if i%2 == 0:
    #     ApplicationStatus.objects.get_or_create(student_id=userProfile, attempt=2,
    #                                           level=1, status=1, description="Hello",
    #                                           campus=0, natureOfQuery=0)
    #     if i%3 == 0:
    #       ApplicationStatus.objects.get_or_create(student_id=userProfile, attempt=3,
    #                                           level=1, status=1, description="Hello",
    #                                           campus=0, natureOfQuery=0)



  def handle(self, *args, **options):
    self._create()
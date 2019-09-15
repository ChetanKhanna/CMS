from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from grievance.models import UserProfile

class Command(BaseCommand):
  def _create(self):
    for i in range(10):
      user = User.objects.get_or_create(username="user"+str(i),password="123456")
      user=User.objects.get(username="user"+str(i))
      UserProfile.objects.get_or_create(user = user, token=0, name="Name "+str(i), contact="9876543210", email="user@mail.com", campus=0)
    
  def handle(self, *args, **options):
    self._create()
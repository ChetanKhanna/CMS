from django.core.management.base import BaseCommand
from grievance.models import *
from django.contrib.auth.models import User

class Command(BaseCommand):
	def _create(self):
		GrievanceForm.objects.all().delete()
		UserProfile.objects.all().delete()
		ApplicationStatus.objects.all().delete()
		InformativeQueryForm.objects.all().delete()
		User.objects.all().exclude(is_staff=True, is_superuser=True).delete()

	def handle(self, *args, **options):
		self._create()

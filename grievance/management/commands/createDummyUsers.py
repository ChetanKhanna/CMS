from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from grievance.models import UserProfile, GrievanceForm, ApplicationStatus
from django.utils.crypto import get_random_string


class Command(BaseCommand):
	def _create(self):
		pass
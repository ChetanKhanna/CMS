from django.core.management.base import BaseCommand
from grievance.models import *
import csv
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from grievance.views import constants

#import for base directory address
from django.conf import settings
BASE_DIR = settings.BASE_DIR

class Command(BaseCommand):
	def _create(self):
		i = 0
		filename = 'data.csv'
		file = os.path.join(BASE_DIR+"/media", filename)
		with open(file) as data_file:
			reader = csv.reader(data_file)
			for column in reader:
				token = constants.UserType.STUDENT.value
				username = column[0]
				name = column[1]
				contact = column[3]
				email = column[4]
				cg = column[2]
				campus = self.getCampus(username)
				user = None
				try:
					(user, created) = User.objects.get_or_create(username = username, email = email) 
					user.set_password(get_random_string(8))
					user.save()
				except:
					pass

				try:
					(_, _) = UserProfile.objects.get_or_create(user = user, token = token, name = name, contact = contact, email = email, campus = campus, cg = cg)
				except:
					pass

				print(i)
				i = i + 1

	def handle(self, *args, **options):
		self._create()

	def getCampus(self, id):
		campus = None
		if id[-1] == 'G':
			campus = constants.Campus.GOA.value
		elif id[-1] == 'P':
			campus = constants.Campus.PILANI.value
		elif id[-1] == 'H':
			campus = constants.Campus.HYDERABAD.value

		return campus
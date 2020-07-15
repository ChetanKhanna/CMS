from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import User

import csv
import os

BASE_DIR = settings.BASE_DIR


class Command(BaseCommand):
    def _activate(self):
        filename = 'batch.csv'
        f = os.path.join(BASE_DIR, 'media', filename)
        with open(f) as data_file:
            reader = csv.reader(data_file)
            next(reader) # skipping the header row
            for col in reader:
                username = col[0]
                try:
                    user = User.objects.get(username=username)
                    user.is_active = True
                    user.save()
                except Exception as e:
                    print(e)
                    print(username, 'NOT activated!')
                else:
                    print(username, 'activated successfully!')

    def handle(self, *args, **kwargs):
        self._activate()


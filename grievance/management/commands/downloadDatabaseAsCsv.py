from django.core.management.base import BaseCommand
from django.conf import settings

from grievance.models import UserProfile, GrievanceForm, ApplicationStatus
from grievance.views import constants

import csv
import os

BASE_DIR = settings.BASE_DIR

class Command(BaseCommand):
        def _create(self):
                # finding name of file
                file_name = 'database.csv'
                file_path = os.path.join(BASE_DIR + '/media/', file_name)
                # writting headers to csv
                with open(file_path, 'w+', encoding='utf-8') as databaseEntriesAsCsv:
                        fieldnames = [
                                'BITS_ID','Name','CGPA','Campus','Alloted_Station',
                                'Preference_Number_Of_Allocated_Station', 'Nature_Of_Query','Description',
                                ]
                        entry_writer = csv.DictWriter(databaseEntriesAsCsv, fieldnames=fieldnames)
                        entry_writer.writeheader()
                # writting data into csv
                with open(file_path, mode='a', encoding='utf-8') as databaseEntriesAsCsv:
                        entry_writer = csv.writer(databaseEntriesAsCsv, delimiter=',', quotechar='"',
                                                        quoting=csv.QUOTE_MINIMAL)
                        for student in UserProfile.objects.all() :
                                row = []
                                try:
                                        grievance_form = GrievanceForm.objects.get(student_id = student)
                                        app_status = ApplicationStatus.objects.get(student_id = student)
                                except Exception as e:
                                        print(e)
                                        print('Unable to fetch details of {}'.format(student.user.username))
                                else:
                                        try:
                                                # UserProfile model fields
                                                row.append((student.user.username).encode('utf-8'))
                                                row.append((student.name).encode('utf-8'))
                                                row.append((student.cg).encode('utf-8'))
                                                campus = constants.Campus._value2member_map_[student.campus].name
                                                row.append((campus).encode('utf-8'))
                                                # GrievanceForm model fields
                                                row.append(str(grievance_form.allocatedStation).encode('utf-8'))
                                                row.append(str(grievance_form.preferenceNumberOfAllocatedStation).encode('utf-8'))
                                                nature_of_query = constants.NatureOfQuery._value2member_map_[
                                                        grievance_form.natureOfQuery].name
                                                row.append(str(nature_of_query).encode('utf-8'))
                                                # ApplicationStatus model fields
                                                row.append((app_status.description).encode('utf-8'))
                                                entry_writer.writerow(row)
                                        except Exception as e:
                                                print(e)
                                                print('Unable to write details of {} in csv'.format(student.user.username))
                                        else:
                                                print(student.user.username)
                return 1

        def handle(self, *args, **options):
                self._create()
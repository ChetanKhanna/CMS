from django.core.management.base import BaseCommand
from grievance.models import *
import csv
import os
from django.conf import settings

BASE_DIR = settings.BASE_DIR

class Command(BaseCommand):
        def _create(self):
                # finding name of file
                file_name = 'databaseEntriesAsCsv.csv'
                # folder_name = 'myproject'
                file_path = os.path.join(BASE_DIR, file_name)
                # writting headers to csv
                with open(file_path, 'w+', encoding='utf-8') as databaseEntriesAsCsv:
                        fieldnames = [
                                'Student_ID','Name','Campus','Attempt','Level','Status','Description','Level1Comment','Level2Comment','NewStation','NatureOfQuery','Publish','LastChangedDate',
                                'preferedStation1','preferedStation2','preferedStation3','preferedStation4','preferedStation5','preferedStation6','preferedStation7','preferedStation8','preferedStation9',
                                'preferedStation10','priority','preferenceNumberOfAllocatedStation',
                                'InformativeAttempt','InformativeStatus','InformativeDescription','InformativeComment','InformativeLastChangedDate',
                                ]
                        entry_writer = csv.DictWriter(databaseEntriesAsCsv, fieldnames=fieldnames)
                        entry_writer.writeheader()
                # writting data into csv
                with open(file_path, mode='a', encoding='utf-8') as databaseEntriesAsCsv:
                        entry_writer = csv.writer(databaseEntriesAsCsv, delimiter=',', quotechar='"',
                         quoting=csv.QUOTE_MINIMAL)
                        i = 1
                        for student in UserProfile.objects.all() :
                                for attempts in range (1,4):
                                        toWrite = list()
                                        try:
                                                GrievanceFormob = GrievanceForm.objects.get(student_id = student)
                                                l=0
                                        except:
                                                pass
                                                l=1
                                        try:
                                                appstatus = ApplicationStatus.objects.get(student_id = student, attempt = attempts)
                                                k=0
                                        except:
                                                pass                
                                                k=1
                                        try:
                                                informativeQueryFormOb = InformativeQueryForm.objects.get(student_id = student, attempt = attempts)
                                                j=0
                                        except:
                                                pass     
                                                j=1
                                        if(l==0 or j==0):
                                                toWrite.append((student.user.username).encode('utf-8'))
                                                toWrite.append((student.name).encode('utf-8'))
                                        else:
                                                break
                                        if(k==1 and j==1):
                                                break
                                        if(k==0):
                                                toWrite.append(str(appstatus.campus).encode('utf-8'))
                                                toWrite.append(str(appstatus.attempt).encode('utf-8'))
                                                toWrite.append(str(appstatus.level).encode('utf-8'))
                                                toWrite.append(str(appstatus.status).encode('utf-8'))
                                                toWrite.append((appstatus.description).encode('utf-8'))
                                                toWrite.append((appstatus.level1Comment).encode('utf-8'))
                                                toWrite.append((appstatus.level2Comment).encode('utf-8'))
                                                toWrite.append((appstatus.newStation).encode('utf-8'))
                                                toWrite.append(str(appstatus.natureOfQuery).encode('utf-8'))
                                                toWrite.append(str(appstatus.publish).encode('utf-8'))
                                                toWrite.append(str(appstatus.lastChangedDate).encode('utf-8'))
                                        else:
                                                for z in range(0,11):
                                                        toWrite.append(''.encode('utf-8'))
                                        if(l==0):        
                                                toWrite.append((GrievanceFormob.preferedStation1).encode('utf-8'))
                                                toWrite.append((GrievanceFormob.preferedStation2).encode('utf-8'))
                                                toWrite.append((GrievanceFormob.preferedStation3).encode('utf-8'))
                                                toWrite.append((GrievanceFormob.preferedStation4).encode('utf-8'))
                                                toWrite.append((GrievanceFormob.preferedStation5).encode('utf-8'))
                                                toWrite.append((GrievanceFormob.preferedStation6).encode('utf-8'))
                                                toWrite.append((GrievanceFormob.preferedStation7).encode('utf-8'))
                                                toWrite.append((GrievanceFormob.preferedStation8).encode('utf-8'))
                                                toWrite.append((GrievanceFormob.preferedStation9).encode('utf-8'))
                                                toWrite.append((GrievanceFormob.preferedStation10).encode('utf-8'))
                                                toWrite.append(str(GrievanceFormob.priority).encode('utf-8'))
                                                toWrite.append(str(GrievanceFormob.preferenceNumberOfAllocatedStation).encode('utf-8'))
                                        else:
                                                for z in range(0,12):
                                                        toWrite.append(''.encode('utf-8'))        
                                        
                                        if(j==0):
                                                toWrite.append(str(informativeQueryFormOb.attempt).encode('utf-8'))
                                                toWrite.append(str(informativeQueryFormOb.status).encode('utf-8'))
                                                toWrite.append((informativeQueryFormOb.description).encode('utf-8'))
                                                toWrite.append((informativeQueryFormOb.level1Comment).encode('utf-8'))
                                                toWrite.append(str(informativeQueryFormOb.lastChangedDate).encode('utf-8'))
                                        else:
                                                for z in range(0,5):
                                                        toWrite.append(''.encode('utf-8'))        
                                        # toWrite.append((station.station_name).encode('utf-8'))
                                        # toWrite.append((station.station_address).encode('utf-8'))
                                        # toWrite.append((mentor.mentor_name).encode('utf-8'))
                                        # toWrite.append((mentor.mentor_id).encode('utf-8'))
                                        # toWrite.append((mentor.mentor_contact).encode('utf-8'))
                                        # toWrite.append((mentor.mentor_email).encode('utf-8'))
                                        # Write the writter object to file
                                        print(i)
                                        i=i+1
                                        if(l==0 or j==0):
                                                entry_writer.writerow(toWrite)      
                return 1

        def handle(self, *args, **options):
                self._create()
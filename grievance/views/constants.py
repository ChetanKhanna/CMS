import enum
class UserType(enum.Enum):
	STUDENT = 0
	CMO = 1
	AD = 2
	ALLOCATIONTEAM = 3
	SUPERUSER = 4
	ADMIN = 5

class NatureOfQuery(enum.Enum):
	MEDICAL=0
	NONMEDICAL=1

class Campus(enum.Enum):
	GOA=0
	HYDERABAD=1
	PILANI=2

class Priority(enum.Enum):
	LOW=0
	MEDIUM=1
	HIGH=2

class Status(enum.Enum):
	NOAPPLICATION=0
	INPROGRESS=1
	PENDING=1
	APPROVED=2
	REJECTED=3

class Publish(enum.Enum):
	PUBLISHED=1
	UNPUBLISHED=0
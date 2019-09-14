import enum
class UserType(enum.Enum):
	STUDENT = 1
	CMO = 2
	AD = 3
	ALLOCATIONTEAM = 4
	SUPERUSER = 5
	ADMIN = 6	

class NatureOfQuery(enum.Enum):
	MEDICAL=1
	NONMEDICAL=0

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
	APPROVED=2
	REJECTED=3
	
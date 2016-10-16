from enum import Enum
from datetime import datetime


class Eligibility(Enum):
	eligible = "eligible"
	ineligible = "ineligible"
	coach_petitions = "coach petitions"


def get_eligibility(dob: datetime, dos: datetime, course_count: int) -> Eligibility:
	if (dos.year >= 2010) or (dob.year >= 1991):
		return Eligibility.eligible
	elif course_count > (8 * 5):
		return Eligibility.ineligible
	else:
		return Eligibility.coach_petitions


t = int(input())
for _ in range(t):
	s = input()
	s = s.split()
	name = s[0]
	studies_start = datetime.strptime(s[1], "%Y/%m/%d")
	birthdate = datetime.strptime(s[2], "%Y/%m/%d")
	courses = int(s[3])
	eligibility = get_eligibility(birthdate, studies_start, courses)
	print(name, eligibility.value)

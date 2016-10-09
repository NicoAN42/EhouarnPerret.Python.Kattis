# no mutable tuples on Kattis available
# could be recordclass but requires to install an additional package


class Problem(object):
	def __init__(self, m, s):
		self.minutes = m
		self.success = s


problems = dict()
score = 0
problem_count = 0
while True:
	entry = input()
	if entry == "-1":
		break
	else:
		entry = entry.split()
		minutes = int(entry[0])
		name = entry[1]
		success = True if entry[2] == "right" else False
		print(minutes, name, success)
		if name not in problems:
			if success:
				problems[name] = Problem(minutes, success)
				score += minutes
				problem_count += 1
			else:
				problems[name] = Problem(20, success)
		else:
			if not problems[name].success:
				if success:
					problems[name].success = success
					problems[name].minutes += minutes
					score += problems[name].minutes
					problem_count += 1
				else:
					problems[name].minutes += 20
print(problem_count, score)

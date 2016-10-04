class Problem(object):
	def __init__(self, name, time, ):

		pass



d = dict()
result = 0
while True:
	log = input()
	if log == "-1":
		break
	else:
		log = log.split()
		m = int(log[0])
		p = log[1]
		o = True if log[1] == "right" else False


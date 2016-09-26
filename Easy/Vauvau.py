def get_status(person, d1a, d1c, d2a, d2c):
	pass


a, b, c, d = map(int, input().split())
guys = map(int, input().split())
for guy in guys:
	status = get_status(guy, a, b, c, d)
	print(status)

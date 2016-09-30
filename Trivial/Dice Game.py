gunnar = map(int, input().split())
emma = map(int, input().split())
gunnar = sum(gunnar)
emma = sum(emma)
if gunnar > emma:
	print("Gunnar")
elif gunnar < emma:
	print("Emma")
else:
	print("Tie")

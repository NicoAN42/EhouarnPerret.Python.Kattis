def get_dog_status(time, dog_aggr, dog_calm):
	period = dog_aggr + dog_calm
	remainder = time % period
	return True if (0 < remainder <= dog_aggr) else False


def get_status(time, dog1_aggr, dog1_calm, dog2_aggr, dog2_calm):
	dog1_status = get_dog_status(time, dog1_aggr, dog1_calm)
	dog2_status = get_dog_status(time, dog2_aggr, dog2_calm)
	if dog1_status and dog2_status:
		return "both"
	elif dog1_status or dog2_status:
		return "one"
	else:
		return "none"


a, b, c, d = map(int, input().split())
pmg = map(int, input().split())
for guy in pmg:
	status = get_status(guy, a, b, c, d)
	print(status)

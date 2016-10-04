n = int(input())
s = input()
t = [int(token) for token in s.split()]
# reversed cause the tree that need a lot of time to fully grow
# should be planted first in order to optimize the planting strategy
t.sort(reverse=True)
# a least the day after the last tree has growth
party = 1
# the last day of growth of the tree the less optimized
max_t = 1 + t[0]
for ti in t:
	party += 1
	max_t = max(max_t, party + ti)
print(max_t)

n = int(input())
simon_says = "Simon says"
for _ in range(n):
	s = input()
	if s.startswith(simon_says):
		words = s[len(simon_says):]
		print(words)

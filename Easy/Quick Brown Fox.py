import string


def is_pangram(phrase):
	alphabet = set(string.ascii_lowercase)
	occurences = set()
	for letter in phrase:
		letter = letter.lower()
		if (letter in alphabet) and (letter not in occurences):
			occurences.add(letter)
	missing_letters = sorted(alphabet - occurences)
	return missing_letters


n = int(input())
for _ in range(n):
	phrase = input()
	result = is_pangram(phrase)
	if len(result) == 0:
		print("pangram")
	else:
		print("missing", "".join(result))

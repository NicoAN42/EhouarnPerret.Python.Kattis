vowels = {"a", "e", "i", "o", "u"}


def is_vowel(letter):
	return letter in vowels


enciphered = input()
deciphered = ""
i = 0
n = len(enciphered)
while i < n:
	character = str(enciphered[i])
	deciphered += character
	if is_vowel(character):
		i += 3
	else:
		i += 1
print(deciphered)

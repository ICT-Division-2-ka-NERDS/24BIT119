# Que-1

s = input("Enter a string: ").lower()

vowels = "aeiou"

no_of_vowels = 0

for i in vowels:
    no_of_vowels += s.count(i)

print("Number of vowels: ", no_of_vowels)
# Pangram is a sentence that uses every letter of the alphabet. Write a program to check whether a given string is pangram or not, through a user-defined function ispangram(). Test the function with “The quick brown fox jumps over the lazy dog” or “Crazy Fredrick bought many very exquisite opal jewels”. Hint: use set() to convert the string into a set of characters present in the string and use <= to check whether alphaset is a subset of the given string.
def ispangram(s):
    alpha = set([chr(x) for x in range(97,123)])
    s = s.replace(" ",'')
    s = set(s.lower())
    return True if alpha == s else False

print(ispangram("The quick brown fox jumps over the lazy dog"))
# 24bit119

# Recursive_Que-3

def count_vowels(string:str):
    if string == "":
        return 0
    elif string[0] in "aeiouAEIOU":
        return 1 + count_vowels(string[1:])
    else:
        return count_vowels(string[1:])
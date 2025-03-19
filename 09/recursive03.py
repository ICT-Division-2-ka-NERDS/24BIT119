# A string is entered through the keyboard. Write a recursive function that counts the number of vowels in this string.

def count_vowels(string:str):
    if string == "":
        return 0
    elif string[0] in "aeiouAEIOU":
        return 1+count_vowels(string[1:])
    else:
        return count_vowels(string[1:])
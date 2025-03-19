# A palindrome is a word or phrase that reads the same in both directions. Write a program that defines a function ispalindrome() which checks whether a given string is a palindrome or not. Ignore spaces and case mismatch while checking for palindrome.
def ispalindrome(s):
    return s == s[::-1]

print(ispalindrome(input("Enter string: ")))
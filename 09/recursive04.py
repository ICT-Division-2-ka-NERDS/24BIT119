# Write a recursive function that reverses the list of numbers that it receives.

def reverse(l):
    if len(l) == 0:
        return l
    else:
        return reverse(l[1:]) + [l[0]]
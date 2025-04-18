# 24bit119

# Recursive_Que-4

def reverse(l):
    if len(l) == 0:
        return l
    else:
        return reverse(l[1:]) + [l[0]]
# 24bit119

# Recursive_Que-6

def sanitize_list(l):
    if len(l) == 0:
        return l
    elif l[0] < 0:
        return [0] + sanitize_list(l[1:])
    
# print(sanitize_list([1, -2, 3, -4, 5]))
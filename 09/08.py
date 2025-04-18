# 24bit119

# Que-8
def convert():
    s = input("Enter string here: ")
    l = s.split()
    l = list(set(l))
    l.sort()
    print(l)
convert()
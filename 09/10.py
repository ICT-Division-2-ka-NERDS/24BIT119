# Write a program that defines a function called frequency() which computes the frequency of words present in a string passed to it. The frequencies should be returned in sorted order of words in the string.
def frequency(s):
    l = s.split()
    l.sort()
    d = {}
    for ele in l :
        d[ele] = l.count(ele)
    for k,v in d.items():
        print(f"{k}: {v}")

frequency("apple apple orange orange orange apple guava guava")
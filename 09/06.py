# Write a function to create and return a list containing tuples of the form (x,x2,x3) for all x between 1 and given ending value (both inclusive).
def ind(end):
    l = []
    for x in range(1,end+1):
        l.append((x,x*x,x**3))
    return l

end = int(input("Enter the end number: "))
print(ind(end))
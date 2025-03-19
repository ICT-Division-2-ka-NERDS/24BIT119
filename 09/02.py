# Write a program that defines a function compute() that calculates the value of n + nn + nnn + nnnn, where n is digit received by the function. test the function for digits 4 to 7.
def compute(n):
    sum = 0
    for i in range(1,n+1):
        sum += int(str(n)*i)
    return sum

for n in range(4,8):
    print(n,compute(n),sep=' : ')
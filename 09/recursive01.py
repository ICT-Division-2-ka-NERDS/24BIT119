# If a positive integer is entered through the keyword, write a recursive function to obtain the prime factors of the number.
def factors(n):
    l = []
    for i in range(1,n):
        if n%i == 0 and is_prime(i):
            l.append(i)
    return l

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(factors(int(input("Enter a number: "))))
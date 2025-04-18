# 24bit119

# Recursive_Que-1
def prime_factors(n, i=2):
    if n == 1:
        return []
    elif n%i == 0:
        return list(set([i] + prime_factors(n//i, i)))
    else:
        return prime_factors(n, i+1)

for i in range(1, 100):
    print(f"{i}: {prime_factors(n=i)}")
# 24bit119

# Recursive_Que-7

def avg(l,n=0, sum = 0):
    print(len(l))
    if len(l) >= 1:
        # print(f"sum= {sum}, n={n}")
        return avg(l[1:], n+1, sum + l[0])
    else:
        print(f"sum={sum}, n={n}")
        return sum/n

print(avg([1,2,3,4,5]))
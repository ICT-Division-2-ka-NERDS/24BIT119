# 24bit119

# Recursive_Que-5

def calculate_power(a=int(input("Enter base: ")), b=int(input("Enter power: "))):
    if b == 0:
        return 1
    else:
        return a*calculate_power(a, b-1)

print(calculate_power())
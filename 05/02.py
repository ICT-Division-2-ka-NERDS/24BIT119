# Que-2

import random

l1 = random.choices(range(1,11),k=20)
print(l1)
num = int(input("Enter a number: "))
print(l1.count(num))
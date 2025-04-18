# 24bit119

# Que-3

import random

l1 = random.choices(range(1,31),k=50)
l1.sort()
print("Sorted before removing duplicates",l1,sep="\n")

for i in l1:
    while l1.count(i) > 1:
        l1.remove(i)

print("After removing duplicates",l1,sep="\n")
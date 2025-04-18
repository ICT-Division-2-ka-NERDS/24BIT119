# 24bit119

# Que-4

import random

l = random.choices(range(-100,101),k=30)
l1,l2=[],[]
print(l)

for i in l:
    if i <0:
        l1.append(i)
    else:
        l2.append(i)

print(f'+Ve nos.: {l1}',f'-Ve nos.: {l2}',sep='\n')
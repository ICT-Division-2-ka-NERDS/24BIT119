# Que-1

import random
l1 = random.choices(range(1,100,2),k=5)
l2 = random.choices(range(2,100,2),k=4)

print("Two lists:",l1,l2,sep='\n')

# l1[2] = l2
# print('After replacing',l1,l2,sep='\n')

new_l = l1[:2] + l2 + l1[3:]
print('After adding, flattening and sorting',new_l,sep='\n')
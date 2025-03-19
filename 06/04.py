# Que-4

import operator

food = [("apple",100),("banana",200),("orange",300),("kiwi",400),("grape",500)]
food1 = []
food2 = []
# food.sort(key = lambda x:x[1],reverse=True)

# food.sort(key = operator.itemgetter(1),reverse=True)

for ele in food:
    ele = list(ele)
    ele[0],ele[1] = ele[1],ele[0]
    food1.append(ele)

food1.sort(reverse=True)

for ele in food:
    ele = list(ele)
    ele[0],ele[1] = ele[1],ele[0]
    food2.append(tuple(ele))

print(food2)
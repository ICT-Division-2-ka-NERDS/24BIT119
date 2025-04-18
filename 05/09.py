# 24bit119

# Que-9

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = []

for num in list1:
    if num not in list2:
        list3.append(num)

print(list3)
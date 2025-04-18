# 24bit119

# Que-2

import csv

d = {"Roll No": [], "Name": [], "Marks 1": [], "Marks 2": [], "Marks 3": [], "Total": []}
total = 0

with open("10/02-file.csv", "r", newline="") as f:
    data = list(csv.reader(f))
    seeker = data.pop(0)
    for line in data:
        d["Roll No"].append(int(line[0]))
        d["Name"].append(line[1])
        d["Marks 1"].append(int(line[2]))
        d["Marks 2"].append(int(line[3]))
        d["Marks 3"].append(int(line[4]))
        total = int(line[2]) + int(line[3]) + int(line[4])
        d["Total"].append(total)


print('\n\n')
# for k in d.keys():
#     for v in d[k]:
#         print(v, end=" ")
#     print()

print(d)
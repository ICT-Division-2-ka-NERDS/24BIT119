# Que-5

names = [("b1",), "g1", ("b2",), "g2", ("b3",), "g3", ()]

for name in names:
    if name == ():
        names.remove(name)
print(names)
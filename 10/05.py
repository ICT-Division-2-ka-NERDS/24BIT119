# 24bit119

# Que-5

with open("05-file1.txt", "r") as f:
    file1 = f.read().upper()

with open("05-file2.txt", "w") as f:
    f.write(file1)

print(file1)
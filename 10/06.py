# 24bit119

# Que-6

def merge_files(file1_path, file2_path, output_path):
    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2, open(output_path, 'w') as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        max_len = max(len(lines1), len(lines2))

        for i in range(max_len):
            if i < len(lines1):
                out.write(lines1[i])
            if i < len(lines2):
                out.write(lines2[i])

    print(f"Merged lines written to {output_path}")

file1 = 'file1.txt'
file2 = 'file2.txt'
output = 'merged_output.txt'

merge_files(file1, file2, output)

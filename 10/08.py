# 24bit119

# Que-8

def remove_articles(input_file, output_file):
    articles = {'a', 'an', 'the'}

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            words = line.split()
            filtered_words = [word for word in words if word.lower() not in articles]
            new_line = ' '.join(filtered_words)
            outfile.write(new_line + '\n')

    print(f"Articles removed and result saved to {output_file}")

input_filename = "file1.txt"
output_filename = "output of 08.txt"
remove_articles(input_filename, output_filename)

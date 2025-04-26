# 24bit119

# Que-4

import os
import shutil

old_folder = "old"
new_folder = "new"
file_to_copy = "file.txt"

os.chdir("./10")
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

from_file = os.path.join(old_folder, file_to_copy)
to_file = os.path.join(new_folder, file_to_copy)

shutil.copy2(from_file, to_file)

print(f"Copied {file_to_copy} to {new_folder}")
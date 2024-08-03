import os
import sys

def delete_duplicates(directory="."):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    file_sizes = {}
    for file in files:
        file_path = os.path.join(directory, file)
        file_size = os.path.getsize(file_path)
        if file_size in file_sizes:
            file_sizes[file_size].append(file_path)
        else:
            file_sizes[file_size] = [file_path]
    for size, files in file_sizes.items():
        if len(files) > 1:
            for file in files[1:]:
                os.remove(file)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        delete_duplicates(sys.argv[1])
    else:
        delete_duplicates()
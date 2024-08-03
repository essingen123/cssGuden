import os
import sys

def rename_jpeg_files(directory="."):
    files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]
    base_name = "party_toad_sticker_fun_fierce_image_photo_fancy_styler_gallery_party_a_"
    for i, file in enumerate(files):
        file_path = os.path.join(directory, file)
        new_name = f"{base_name}{i+1}.jpg"
        os.rename(file_path, os.path.join(directory, new_name))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        rename_jpeg_files(sys.argv[1])
    else:
        rename_jpeg_files()
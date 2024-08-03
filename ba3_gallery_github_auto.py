import os

output_file = 'README.md'
image_formats = ['jpg', 'jpeg', 'gif', 'webp', 'png']
image_path = 'img_trunk_junk'

if not os.path.exists(image_path):
    print(f"Error: Image directory '{image_path}' does not exist. Please create it and add your images.")
    exit(1)

print("## Image Gallery")

with open(output_file, 'a') as f:
    f.write('\n## Image Gallery\n\n')
    for i, file in enumerate((file for file in os.listdir(image_path) if any(file.lower().endswith('.' + fmt) for fmt in image_formats))):
        f.write(f'<img src="{image_path}/{file}" style="width: 30%; margin: 1%; float: left; border-radius: 0.5em;">\n')
        if (i + 1) % 3 == 0:
            f.write('<br>\n')
    f.write('\n')

print(f'Readme file updated: {output_file}')
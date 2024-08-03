import os

output_file = 'README.md'
image_formats = ['jpg', 'jpeg', 'gif', 'webp', 'png']
image_path = 'img_trunk_junk'

if not os.path.exists(image_path):
    print(f"Error: Image directory '{image_path}' does not exist. Please create it and add your images.")
    exit(1)

with open(output_file, 'a') as f:
    f.write('\n## Image Gallery\n\n')
    f.write(f'Note: Images must be placed in the `{image_path}` directory.\n\n')
    for i, file in enumerate((file for file in os.listdir(image_path) if any(file.lower().endswith('.' + fmt) for fmt in image_formats))):
        f.write(f'![]({image_path}/{file}){{:.img-rounded}}\n')
        if (i + 1) % 3 == 0:
            f.write('\n')
    f.write('\n')

print(f'Readme file updated: {output_file}')
import os

output_file = 'README_gallery.md'
image_formats = ['jpg', 'jpeg', 'gif', 'webp', 'png']

with open(output_file, 'w') as f:
    f.write('# Image Gallery\n\n')
    f.write('<div class="gallery">\n')
    for i, file in enumerate((file for file in os.listdir() if any(file.lower().endswith('.' + fmt) for fmt in image_formats))):
        f.write(f'<img src="{file}" alt="{file}" class="img-rounded" style="width: 30%; margin: 1%; float: left;">\n')
        if (i + 1) % 3 == 0:
            f.write('<br>\n')
    f.write('</div>\n')

print(f'Readme file generated: {output_file}')
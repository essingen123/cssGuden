import os
from PIL import Image

output_file = 'README_gallery.md'
image_formats = ['jpg', 'jpeg', 'gif', 'webp', 'png']

with open(output_file, 'w') as f:
    f.write('# Image Gallery\n\n<div class="gallery">\n')
    for file in (file for file in os.listdir() if any(file.lower().endswith('.' + fmt) for fmt in image_formats)):
        img = Image.open(file)
        img.thumbnail((int(img.width * 0.33), int(img.height * (img.width * 0.33) / img.width)))
        img.save(file)
        f.write(f'<img src="{file}" alt="{file}" class="img-rounded" style="width: 30%; margin: 1%; float: left;">\n')
        if (list(os.listdir()).index(file) + 1) % 3 == 0:
            f.write('<br>\n')
    f.write('</div>\n')

print(f'Readme file generated: {output_file}')
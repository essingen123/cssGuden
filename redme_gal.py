import os
from PIL import Image

# Set the output file
output_file = 'README.md'

# Set the image formats
image_formats = ['jpg', 'jpeg', 'gif', 'webp', 'png']

# Create a list to store the image files
image_files = []

# Loop through all files in the current directory
for file in os.listdir():
    # Check if the file has one of the specified formats
    for format in image_formats:
        if file.lower().endswith('.' + format):
            image_files.append(file)
            break

# Create the README.md file
with open(output_file, 'w') as f:
    f.write('# Image Gallery\n\n')

    # Loop through the image files
    for file in image_files:
        # Open the image using PIL
        img = Image.open(file)

        # Resize the image to 33% of the original width
        width, height = img.size
        new_width = int(width * 0.3)
        img = img.resize((300,300))

        # Save the resized image
        img.save(file)

        # Create the Markdown code for the image
        markdown = f'![]({file}){{:.img-rounded}}\n\n'

        # Write the Markdown code to the README.md file
        f.write(markdown)

print(f'Readme file generated: {output_file}')
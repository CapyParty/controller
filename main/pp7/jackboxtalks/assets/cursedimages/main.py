import os
from PIL import Image

# Set target size and format
target_size = (330, 220)
target_format = 'JPEG'

# Get list of all image files in the current directory
supported_extensions = ['.webp', '.png', '.jpg', '.jpeg']
files = [f for f in os.listdir('.') if os.path.isfile(f) and os.path.splitext(f)[1].lower() in supported_extensions]

# Process each file
for file in files:
    # Open the image file
    with Image.open(file) as img:
        # Resize the image to the target size
        img_resized = img.resize(target_size)

        # Define the new filename with .jpg extension
        new_filename = os.path.splitext(file)[0] + '.jpg'

        # Save the resized image in JPEG format
        img_resized.save(new_filename, target_format)

        print(f"Processed and saved {new_filename}")

print("All files processed.")

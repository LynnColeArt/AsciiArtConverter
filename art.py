import argparse
import os
from PIL import Image
import numpy as np

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Convert an image to colored ASCII art and output as HTML.")
parser.add_argument("image_path", help="The relative path to the image file.")
args = parser.parse_args()

# Open image and resize it to the size you want your ascii art to be
img = Image.open(args.image_path).convert("RGBA").resize((320, 160))

# Map from pixel intensity to ASCII characters
ascii_chars = "@%#*+=-:. "

# Create colored ASCII art
ascii_art = ""
for y in range(img.height):
    for x in range(img.width):
        r, g, b, _ = img.getpixel((x, y))
        avg_rgb = int((r + g + b) / 3)  # Calculate average RGB value
        ascii_char = ascii_chars[avg_rgb * (len(ascii_chars) - 1) // 255]  # Map avg_rgb to ASCII char
        ascii_art += '<div class="char" style="color:rgb({},{},{})">{}</div>'.format(r, g, b, ascii_char)
    ascii_art += "<br>"

# Extract base name from the image file path
base_name = os.path.basename(args.image_path)
# Remove the extension
file_name = os.path.splitext(base_name)[0]
# Append .html extension
output_file = file_name + ".html"

# Read the HTML template
with open("ascii.html", "r", encoding="utf-8") as f:
    html_template = f.read()

# Substitute the placeholder with the ASCII art
#html = html_template.format(ascii_art)
html = f"{html_template.replace('{}', ascii_art)}"


# Write the final HTML to a file
with open(output_file, "w") as f:
    f.write(html)

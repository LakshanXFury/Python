from PIL import Image, ImageDraw, ImageFont, ImageColor

# Load the image
image = Image.open("C:/Users/lakshas/Downloads/error teams.png").convert("RGBA")  # Ensure image is RGBA


# Create a new image with transparent background for watermark
watermark = Image.new("RGBA", image.size, (255, 255, 255, 0))

# Create a drawing context
draw = ImageDraw.Draw(watermark)

# Watermark text
watermark_text = "Lakshan"

# Choose a font and size (Ensure you have a font file like Arial.ttf)
font = ImageFont.truetype("arial.ttf", 36)

# Color
color = ImageColor

# Get image dimensions
width, height = image.size

# Get text bounding box (Pillow 10+ fix)
bbox = draw.textbbox((0, 0), watermark_text, font=font)
text_width = bbox[2] - bbox[0]  # Width
text_height = bbox[3] - bbox[1]  # Height

# Position the watermark at the bottom-right corner
x = width - text_width - 10
y = height - text_height - 10

# Add watermark text
draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))  # White with transparency

# Combine watermark with original image
watermarked_image = Image.alpha_composite(image, watermark)

# Convert to RGB before saving as JPEG (Fixes RGBA issue)
watermarked_image = watermarked_image.convert("RGB")
watermarked_image.save("C:/Users/lakshas/Downloads/watermarked_image.jpg")

# Show the image
watermarked_image.show()

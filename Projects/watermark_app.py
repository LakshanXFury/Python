from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageColor

window = Tk()
window.title("Watermark App")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)  # Padding

# Load the image using PIL (for PNG, JPG, etc.)
original_image = Image.open("C:/Users/lakshas/Downloads/ghost_of_tushima.jpg").convert("RGBA")  # Ensure image is RGBA

# Resize image (optional)
resize_image = original_image.resize((400, 300))  # Adjust size as needed

# Convert to Tkinter-compatible format
image_path = ImageTk.PhotoImage(resize_image)

# Label for the app
main_label = Label(text="Upload an image to add the watermark", font=("Arial", 20, "bold"))
main_label.grid(row=0, column=0, columnspan=2, pady=10)  # Use .grid() instead of .pack()

# Load Image Label
load_image = Label(window, image=image_path)
load_image.image = image_path  # Keep a reference to avoid garbage collection
load_image.grid(row=1, column=0,
                columnspan=2)  # When you set columnspan=N, the widget will occupy N columns instead of just one.


# Button Function
def button_clicked():
    print("Clicked me")
    # Create a new image with transparent background for watermark
    watermark = Image.new("RGBA", original_image.size, (255, 255, 255, 0))

    # Create a drawing context
    draw = ImageDraw.Draw(watermark)

    # Watermark text
    watermark_text = "Lakshan"

    # Choose a font and size (Ensure you have a font file like Arial.ttf)
    font = ImageFont.truetype("arial.ttf", 24)

    # Color
    color = ImageColor

    # Get image dimensions
    width, height = original_image.size

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
    watermarked_image = Image.alpha_composite(original_image, watermark)

    # Convert to RGB before saving as JPEG (Fixes RGBA issue)
    watermarked_image = watermarked_image.convert("RGB")
    watermarked_image.save("C:/Users/lakshas/Downloads/watermarked_image.jpg")

    # Show the image
    watermarked_image.show()


# Button
btn = Button(text="Click me", command=button_clicked)
btn.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()

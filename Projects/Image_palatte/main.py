from flask import Flask, render_template, request
import os
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    print("Upload route hit")
    file = request.files.get('image')  # This image is coming from the HTML.
    file.stream.seek(0)
    if file:
        colors = image_palette(file)
        return render_template("index.html", colors=colors)
    return "No image uploaded", 400


def image_palette(uploaded_image):
    # Load image using Pillow
    image = Image.open(uploaded_image)
    image = image.convert('RGB')  # 👈 This ensures it's in RGB mode
    image = image.resize((200, 200))  # Resize for faster processing

    # Convert image to NumPy array
    pixels = np.array(image).reshape(-1, 3)

    # Apply KMeans clustering
    k = 10  # Number of dominant colors
    kmeans = KMeans(n_clusters=k, n_init='auto')
    kmeans.fit(pixels)

    # Get dominant colors
    colors = kmeans.cluster_centers_.astype(int)

    hex_colors = ['#%02x%02x%02x' % tuple(color) for color in colors]

    # # Display the colors
    # for i, color in enumerate(colors):
    #     plt.subplot(1, k, i + 1)
    #     plt.imshow([[color / 255]])
    #     plt.axis('off')
    # plt.show()

    return hex_colors


if __name__ == "__main__":
    app.run(debug=True)

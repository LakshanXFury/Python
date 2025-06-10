import fitz
import pyttsx3
from tkinter import Tk, filedialog, Button, Label

window = Tk()
window.title("Text to Speech Converter")
window.minsize(width=1000, height=600)
window.config(padx=50, pady=50)


# File Upload
def upload_pdf():
    file_path = filedialog.askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF files:", "*.pdf")]
    )
    if file_path:
        print("Selected File: ", file_path)

    read_the_text(file_path)


def read_the_text(path):
    doc = fitz.open(f"{path}")
    for page in doc:
        text = page.get_text()
        print(text)

        tts(text)
    doc.close()


def tts(speech):
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()


# Label
my_label = Label(text="Upload the file to Read the text from PDF", font=("Arial", 24, "bold"))
my_label.pack()

# Upload button
upload_btn = Button(window, text="Upload PDF", command=upload_pdf)
upload_btn.pack(pady=40)

window.mainloop()

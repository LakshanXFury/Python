from tkinter import *
import time
import random

# Sample text to type
sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Programming is an art of thinking, not typing.",
    "Speed is useful only if you are running in the right direction.",
    "Python is a powerful and versatile programming language."
]


class TypingSpeedTest:
    def __init__(self, window):
        self.root = window
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")
        self.root.config(padx=20, pady=20)

        self.start_time = None
        self.selected_text = random.choice(sample_texts)

        # Title label
        self.title_label = Label(text="Typing speed test", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        # Display Sample text
        self.text_label = Label(text=self.selected_text, font=("Arial", 14, "bold"), wraplength=500, justify="center")
        self.text_label.pack(pady=10)

        #Input Box
        self.input_text = Text(height=4, width=50, font=("Arial", 12))
        self.input_text.pack(pady=10)
        self.input_text.bind("<KeyPress", self.start_timer)   # Start timer when user starts typing





window = Tk()
app = TypingSpeedTest(window)
# Run Tkinter
window.mainloop()

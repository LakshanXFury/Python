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
        self.input_text.bind("<KeyPress>", self.start_timer)  # Start timer when user starts typing

        # Submit Button
        self.submit_button = Button(text="Check Speed", command=self.calculate_speed)
        self.submit_button.pack(pady=5)

        # Result Label
        self.result_label = Label(text="", font=("Arial", 14, "bold"), fg="green")
        self.result_label.pack(pady=10)

        # Retry Button
        self.retry_button = Button(text="Retry", command=self.reset_test)
        self.retry_button.pack(pady=5)

    def start_timer(self, event):
        """Starts the timer when the user begins typing"""
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self):
        """Calculates typing speed in WPM and accuracy"""
        if self.start_time is None:
            return

        end_time = time.time()
        total_time = end_time - self.start_time  # Time taken in seconds
        user_input = self.input_text.get("1.0", "end-1c")  # Get user input

        word_count = len(user_input.split())  # Count words typed
        time_in_minutes = total_time / 60
        if time_in_minutes > 0:
            wpm = round(word_count / time_in_minutes)
        else:
            wpm = 0

        # Accuracy Calculation - This line calculates the accuracy of the user's typed input compared to the given text.
        correct_chars = sum(1 for a, b in zip(user_input, self.selected_text) if a == b)
        """
        correct_chars = 0
        for a, b in zip(user_input, self.selected_text):
            if a == b:
                correct_chars += 1 
        """

        accuracy = round((correct_chars / max(len(self.selected_text), 1)) * 100, 2)  # Avoid division by zero, Rounds
        # the result to 2 decimal places for better readability.
        # ,1 ->  Prevents division by zero

        self.result_label.config(text=f"Speed: {wpm} WPM | Accuracy: {accuracy}%")

    def reset_test(self):
        """Resets the test for another attempt"""
        self.start_time = None
        self.selected_text = random.choice(sample_texts)
        self.text_label.config(text=self.selected_text)
        self.input_text.delete("1.0", "end")
        self.result_label.config(text="")


window = Tk()
app = TypingSpeedTest(window) # app is a variable that stores an instance of the TypingSpeedTest class.
# Run Tkinter
window.mainloop()

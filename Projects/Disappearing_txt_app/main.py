from tkinter import *


def on_keypress(event):
    # Cancel the previous timer if it exists
    # This checks if the timer exists and cancels it before starting a new one — this is how you reset the timer every time the user types.
    if hasattr(window, 'typing_timer'):  # This attribute returns true or false
        window.after_cancel(window.typing_timer)  # Cancels the previous time to reset the countdown
    # Start a new timer (5000 ms = 5 seconds)
    window.typing_timer = window.after(5000, user_stopped_typing)


def user_stopped_typing():
    content = text_input.get("1.0", END).strip()  # "1.0" — which means line 1, character 0
    if not content:
        print("User isn't typing and input is empty.")
    else:
        print("User stopped typing. Input was:", content)
        text_input.delete("1.0", END)  # "1.0" — which means line 1, character 0


window = Tk()
window.title("Disappearing Text Writing App")
window.minsize(width=1000, height=600)
window.config(padx=50, pady=50)

# Text widget for multi-line input
text_input = Text(window, width=100, height=30)
text_input.pack()

# Bind keypress event to the Text widget
text_input.bind("<Key>", on_keypress)

# Start the timer even if the user doesn't type
window.typing_timer = window.after(5000, user_stopped_typing)  #Stores the ID of that scheduled task in window.typing_timer.


window.mainloop()

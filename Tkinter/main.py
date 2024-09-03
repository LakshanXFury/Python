from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=1000, height=600)
window.config(padx=100, pady=200)   #padding


#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack() #pack the label to center of the program

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#Button

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    # my_label.config(text="Button got clicked")
    print("I got clicked")

button = Button(text="Click Me", command=button_clicked)
# button.pack()
my_label.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry

input = Entry()
# input.pack()
value = input.get()
print(value)
input.grid(column=2, row=2)

















window.mainloop()   #keeps the window open
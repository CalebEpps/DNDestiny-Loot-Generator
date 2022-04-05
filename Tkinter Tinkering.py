import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello",
                    fg="grey",
                    bg="Black",
                    width=100,
                    height=10)
greeting.pack()

window.mainloop()

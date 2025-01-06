import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Clock")

clock_label = tk.Label(root, font=("Arial", 50), bg="light green", fg="blue")
clock_label.pack( anchor = "center", fill ="both", expand = True)

def update_time():
  current_time = strftime("%H:%M:%S")
  clock_label.config(text=current_time)
  clock_label.after(1000, update_time)

update_time()
root.mainloop()
import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("noted")

    mainframe = ttk.Frame(root)
    mainframe.grid(row=0,column=0)
        
    text = tk.Text(mainframe, bg="black", fg="white")
    text.grid(row=0,column=0)

    root.mainloop()

if __name__ == "__main__":
    main()

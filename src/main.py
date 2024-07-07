import tkinter as tk
from tkinter import filedialog

class NotedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("noted")
        self.root.geometry("400x400")

        self.root.bind('<Control-s>', self.saveNote)
        self.root.bind('<Control-o>', self.loadNote)

        self.text = tk.Text(self.root, wrap=tk.WORD, bg="black", fg="white")
        self.text.pack(expand=True,fill=tk.BOTH)

    def saveNote(self, event):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if filepath:
            with open(filepath, "w") as file:
                file.write(self.text.get(1.0, tk.END))

    def loadNote(self, event):
        filepath = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])

        if filepath:
            with open(filepath, "r") as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())

if __name__ == "__main__":
    root = tk.Tk()
    app = NotedApp(root)
    root.mainloop()

import time
from time import strftime
import tkinter as tk

class TimeApp:
    def __init__(self, root):
        self.root = tk.Tk()
        self.root.title("Digital Clock")
        self.root.configure(bg="#000000")
        self.root.geometry("300x100")
        self.root.resizable(False,False)
        self.root_label = tk.Label(self.root,font= ("Arial",20),fg="Magenta",bg="Black")
        self.root_label.pack(pady=10,anchor="center",fill="both",expand="True")
        self.time()


    def time(self):
        current = strftime("%H:%M:%S")
        self.root_label.config(text = current)
        self.root_label.after(1000,self.time)



if __name__ == "__main__":
    window = TimeApp(tk)
    window.root.mainloop()

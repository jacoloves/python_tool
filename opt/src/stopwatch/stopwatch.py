import tkinter as tk
import time

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        master.geometry("300x150")
        master.titile("ストップウォッチ")
        master.config(bg="black")

def main():
        win = tk.Tk()
        app = Application(master = win)
        app.mainloop()

if __name__ == "__main__":
    main()
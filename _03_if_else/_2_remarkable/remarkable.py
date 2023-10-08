import turtle
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    name = simpledialog.askstring(title='question', prompt="what is your name?")
    if name == "henry":
        messagebox.showinfo(title="answer",message="why r u you doing this HENRY")
    if name == "kasra":
        messagebox.showinfo(title="answer",message="why r u you doing this KASRA")
    if name == "jackson":
        messagebox.showinfo(title="answer",message="why r u you doing this JACKSON")
    if name == "liam":
        messagebox.showinfo(title="answer",message="why r u you doing this LIAM!")






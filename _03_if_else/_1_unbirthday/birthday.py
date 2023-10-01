import turtle
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()

    birthday = simpledialog.askstring(title='question', prompt="when is your birthday?")
    if birthday == "october 1":
        messagebox.showinfo(title="answer",message="happy birthday!")
    else:
            messagebox.showerror(title="answer",message="happy unbirthday")



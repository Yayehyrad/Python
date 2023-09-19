from tkinter import Tk,Button ,Entry , StringVar


class Calculator:
    def __init__(self , master : Tk) -> None:
        master.title("calculator")
        master.geometry("257x420+0+0")
        master.config(bg="gray")
        master.resizable(False,False)

        self.equation = StringVar()
        self.entry_val = ""

        Entry(width=45 , bg="#fff",textvariable=self.equation).place(x=0,y=0)
    def show(self , val):
        self.entry_val += val
        self.equation.set(self.entry_val)

root = Tk()
calc = Calculator(root)
root.mainloop()
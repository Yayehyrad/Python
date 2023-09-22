from tkinter import Tk,Button ,Entry , StringVar


class Calculator:
    arr = [
        {"text":"(","x" : 0 , 'y' : 50 , },
        {"text":")","x" : 90 , 'y' : 50 ,},
        {"text":"%","x" : 180 , 'y' : 50 ,},
        {"text":"1","x" : 0 , 'y' : 125 ,},
        {"text":"2","x" : 90 , 'y' : 125 ,},
        {"text":"3","x" : 180 , 'y' : 125 ,},
        {"text":"4","x" : 0 , 'y' : 200 ,},
        {"text":"5","x" : 90 , 'y' : 200 ,},
        {"text":"6","x" : 180 , 'y' : 200 ,},
        {"text":"7","x" : 0 , 'y' : 275 ,},
        {"text":"8","x" : 90 , 'y' : 275 ,},
        {"text":"9","x" : 180 , 'y' : 275 ,},
        {"text":"0","x" : 0 , 'y' : 350 ,},
        {"text":"-","x" : 90 , 'y' : 350 ,},
        {"text":"+","x" : 180, 'y' : 350 ,},
        {"text":"/","x" : 0 , 'y' : 425 ,},
        {"text":"*","x" : 90 , 'y' : 425 ,},
    ]
     
    def __init__(self , master : Tk ) -> None:
        master.title("calculator")
        master.geometry("257x520+0+0")
        master.config(bg="gray")
        master.resizable(False,False)

        self.equation = StringVar()
        self.entry_val = ""
      
        for text  in self.arr:
             print(text)
             a = text["text"]
             Button(width=11 ,height=4 , text=text['text'],relief="flat" , bg="white",command=lambda:self.show(a)).place(x=text['x'],y=text['y'])
       
        Button(width=8 ,height=1 , text="c",relief="flat" , bg="white",command=self.clear).place(x=185,y=20)
        Button(width=11 ,height=4 , text="=",relief="flat" , bg="white",command=self.solve).place(x=180,y=425)


        Entry(width=45  , bg="#fff",textvariable=self.equation).place(x=0,y=0)
    def show(self , val):
        self.entry_val += val
        self.equation.set(self.entry_val)
    def clear(self):
        self.entry_val = ""
        self.equation.set(self.entry_val)
    def solve(self):
        result = eval(self.entry_val)
        self.equation.set(result)
    


root = Tk()
calc = Calculator(root)
root.mainloop()
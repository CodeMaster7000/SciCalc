from tkinter import *
from numpy import *
from math import *

class SciCalc:
        def __init__(self, master):
            self.master = master
            master.title("Graphical Scientific Calculator")
            self.total = StringVar()
            self.entry = Entry(master, textvariable=self.total, borderwidth=5)
            self.entry.grid(row=0, column=0, columnspan=6, pady=6)
            self.button_creator()
        def button_creator(self):
            b_list = [
                [ 'sin', 'cos', 'tan', 'x²', 'x³'],
                ['log(x)', '1/x', 'x!', 'sqrt', 'cbrt'],
                ['7', '8', '9', 'C'],
                ['4', '5', '6', '*', '/'],
                ['1', '2', '3', '+', '-'],
                ['0', '.', '10^x', '=']
            ]
            for i, row in enumerate(b_list):
                for j, b_text in enumerate(row):
                    button = Button(self.master, text=b_text, width=5, height=3, command=lambda text=b_text: self.click(text))
                    button.grid(row=i + 1, column=j, sticky="nsew")
                self.master.rowconfigure(i + 1, weight=1)
            self.master.columnconfigure(0, weight=1)
            self.master.columnconfigure(1, weight=1)
            self.master.columnconfigure(2, weight=1)
            self.master.columnconfigure(3, weight=1)
            self.master.columnconfigure(4, weight=1)
            self.master.columnconfigure(5, weight=1)
        def click(self, b_text):
            if b_text == '=':
                try:
                    result = eval(self.entry.get())
                    self.total.set(result)
                except:
                    self.total.set("Error!")
            elif b_text == 'C':
                    self.total.set("")
            elif b_text == 'sin':
                try:
                    result = sin(radians(float(self.entry.get())))
                    self.total.set(result)
                except:
                    self.total.set("Error!")
            elif b_text == 'cos':
                try:
                    result = cos(radians(float(self.entry.get())))
                    self.total.set(result)
                except:
                    self.total.set("Error!")
            elif b_text == 'tan':
                try:
                    result = tan(radians(float(self.entry.get())))
                    self.total.set(result)
                except:
                    self.total.set("Error!")
            elif b_text == 'x²':
                try:
                    result = float(self.entry.get()) ** 2
                    self.total.set(result)
                except:
                    self.total.set("Error!")
            elif b_text == 'x³':
                try:
                    result = float(self.entry.get()) ** 3
                    self.total.set(result)
                except:
                    self.total.set("Error!")
            elif b_text == 'log(x)':
                try:
                    result = log(float(self.entry.get()))
                    self.total.set(result)
                except:
                    self.total.set("Error!")
            elif b_text == '1/x':
                try:
                    result = 1 / float(self.entry.get())
                    self.total.set(result)
                except:
                    self.total.set("Error!")
            elif b_text == 'x!':
                try:
                    result = factorial(int(self.entry.get()))
                    self.total.set(result)
                except:
                    self.total.set("Error!")
            elif b_text == 'sqrt':
                try:
                    result = sqrt(float(self.entry.get()))
                    self.total.set(result)
                except:
                    self.total.set("Error!")
            elif b_text == 'cbrt':
                try:
                    result = cbrt(float(self.entry.get()))
                    self.total.set(result)
                except:
                    self.total.set("Error!")
            elif b_text == '10^x':
                 try:
                    result = 10 ** float(self.entry.get())
                    self.total.set(result)
                 except:
                    self.total.set("Error!")
            else:
                self.total.set(self.entry.get() + b_text)

    if __name__ == "__main__":
        root = Tk()
        calc = SciCalc(root)
        root.mainloop()

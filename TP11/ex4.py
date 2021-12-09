import sympy
import tkinter


x = sympy.Symbol('x')

print(sympy.integrate(3/x**2,(x,1,'+oo')))


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """creates three inputs : one for the function to integrate, one for the superior bound and one for the inferior bound"""
        self.input_function = tkinter.Entry(self)
        self.input_function.pack(side="top")
        self.input_sup = tkinter.Entry(self)
        self.input_sup.pack(side="top")
        self.input_inf = tkinter.Entry(self)
        self.input_inf.pack(side="top")
        self.button = tkinter.Button(self, text="Integrate", command=self.integrate)
        self.button.pack(side="top")
        self.output = tkinter.Label(self, text="")
        self.output.pack(side="top")
    
    def integrate(self):
        """integrates the function given by the user using the sympy package."""
        try:
            self.output.config(text=sympy.integrate(sympy.integrate(self.input_function.get()),(x,float(self.input_inf.get()),float(self.input_sup.get()))))
        except:
            self.output.config(text="Error")

def main():
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
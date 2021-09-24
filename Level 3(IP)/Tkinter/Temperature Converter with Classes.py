from tkinter import *

class App:            
        def __init__(self, master):
            self.master = master
            self.title = Label(self.master, text = "Temperature Converter")
            self.title.grid(columnspan = 3)
            
            self.fl = Label(self.master, text = "Fahrenheit")
            self.fl.grid(row = 1, sticky = W)

            self.fev = IntVar()
            self.fe = Entry(self.master, textvariable=self.fev)
            self.fe.grid(row=1, column = 1, sticky = E)
            
            
            self.cl = Label(self.master, text = "Celsius")
            self.cl.grid(row=2, sticky = W)

            self.cev = IntVar()
            self.ce = Entry(self.master, textvariable = self.cev)
            self.ce.grid(row=2,column=1,sticky=E)
            
            self.cb = Button(self.master, command=self.clear, text = "Clear", fg = 'green').grid(row=3)
            self.fs = Button(self.master, command=self.fANDcSubmit, text = "Submit for Any Temp!", fg = "red").grid(row=3, column=1)

        def fsubmit(self):
            self.ft = int(self.fe.get())
            #print(self.fe.get())
            print('Fahrenheit recieved:', self.ft, "degrees.")
            self.ct = (self.ft-32)/1.8
            self.cts = str(self.ct)
            print("Celsius recieved:", self.cts, "degrees.")

        def fANDcSubmit(self):
                self.ft = self.fe.get()
                self.ct = self.ce.get()
                if type(self.ct) is str and len(self.ct) >= 1 and self.ft == "0" or self.ft == " ":
                        print("C->F part")
                        self.ctf = float(self.ct)
                        self.cti = int(self.ctf)
                        print("Celsius recieved:", self.ct, "degrees.")
                        self.ft = (self.cti*1.8)+32
                        self.fts = str(self.ft)
                        print('Fahrenheit recieved:', self.fts, "degrees.")
                        self.fev.set(self.fts)
                elif type(self.ft) is str and len(self.ct) >= 1 and self.ct == "0" or self.ft == " ":
                        print("F->C part")
                        self.ftf = float(self.ft)
                        self.fti = int(self.ftf)
                        print('Fahrenheit recieved:', self.ft, "degrees.")
                        self.ct = (self.fti-32)/1.8
                        self.cts = str(self.ct)
                        print("Celsius recieved:", self.cts, "degrees.")
                        self.cev.set(self.ct)
                        
                        
        def clear(self):
            self.fe.delete(0, END)
            self.ce.delete(0, END)

        
        

root = Tk()
GUI = App(root)
root.mainloop()

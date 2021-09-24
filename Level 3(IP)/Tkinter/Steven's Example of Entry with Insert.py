from tkinter import *
from pprint import pprint

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

def fahrenSubmit():
    ft = int(e1.get())
    print("Fahrenheit recieved:", ft, "degrees.")
    cti = (ft-32)/1.8
    cts = str(cti)
    print("Celsius recieved:", cts, "degrees.")
    e2.insert(10, cts)

master = Tk()
Label(master, text="Fahrenheit").grid(row=0)
Label(master, text="Celsius").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

##pprint(dir(e1))


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)



Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=W, 
                                    pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, 
                                                               column=1, 
                                                               sticky=W, 
                                                               pady=4)

Button(master, text = 'Submit', command = fahrenSubmit).grid(row=3, column = 2, sticky=W, pady=4)

master.mainloop()


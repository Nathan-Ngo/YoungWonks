import tkinter as tk
from pprint import pprint

root = tk.Tk()
root.title("Converter")

def submit():
    global fd
    ft = int(fd.get())
    print(ft)
    convert(ft)

def clear():
    fahrenheitEntry.delete(0, END)

def convert(t):
    ct = ((t-32)*5)/9
    print(ct)

    global ce
    pprint(dir(ce))
    ce.insert(0, str(ct))
        
ft = tk.Label(root, text = "Fahrenheit").grid(row=0, column=0, sticky=tk.W)
fd = tk.StringVar()
fd.set('10')
fe = tk.Entry(root).grid(row = 0, column = 1)

ct = tk.Label(root, text = "Celsius").grid(row = 1, column = 0, sticky=tk.W)
cd = tk.StringVar()
cd.set('20')
ce = tk.Entry(root).grid(row = 1, column = 1)


    
submitButton = tk.Button(root, text = "Submit", fg = "blue", command = submit).grid(row = 2, column = 0)

clearButton = tk.Button(root, text = "Clear", fg = "red", command = clear).grid(row = 2, column = 1)

root.mainloop()

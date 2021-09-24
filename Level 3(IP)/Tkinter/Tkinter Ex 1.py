from tkinter import *
root = Tk()
root.title("Hello World")

packList = []

name_label = Label(root, text="Name")
packList.append(name_label)

name_entry = Entry(root)
packList.append(name_entry)

for loop in range(0,2,1):
    packList[loop].pack()
    
exit_button = Button(root,text = "Exit", fg='red', command=exit)
exit_button.pack(side = LEFT)

def clear():
    name_entry.delete(0, END)

clear_button = Button(root, text = "Clear", fg = "blue", command=clear)
clear_button.pack(side = RIGHT)

def submit():
    a = name_entry.get()
    print("name:", a)

submit_button = Button(root, text = "Submit", fg = "green", command=submit)
submit_button.pack(side = TOP)

root.mainloop()


#Login Application made by Nathan Ngo
#Started on 22/9/21
#Finished on [TBA]
from tkinter import *
root = Tk()
root.title("Login Application")
upd = {"joe1":"f451", "michael2":"1984", "dante3":"inferno", "cory4":"handmaidtale", "dereck5":"newworld"}
def clearEntries():
    uE.delete(0, END)
    pE.delete(0, END)
def submitEntries():
    username = uEV.get()
    password = pEV.get()
    print(username)
    print(password)
lL = Label(root, text = "Please log in.").grid(row=0,column=0,columnspan=2)
uL = Label(root, text = "Username:").grid(row=1,column=0)
uEV = StringVar()
uE = Entry(root, textvariable=uEV).grid(row=1,column=1)
pL = Label(root, text = "Password:").grid(row=2,column=0)
pEV = StringVar()
pE = Entry(root, textvariable=pEV).grid(row=2,column=1)
cB = Button(root, text="Clear your entries.", fg = "#dc143c", command = clearEntries).grid(row=3, column=0)
sB = Button(root, text = "Submit to log in.", fg = "#006400", command = submitEntries).grid(row=3,column=1)
root.mainloop()

from tkinter import *
root = Tk()
root.title("Chessboard")
a = "black"
b = "white"
for row in range(1,9,1):
    for column in range(1,10,1):
        Label(root, bg = a, width=3).grid(row = row*50, column = column*50)
        a, b = b, a
root.mainloop()

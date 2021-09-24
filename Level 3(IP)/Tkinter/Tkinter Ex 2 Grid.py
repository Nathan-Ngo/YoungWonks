from tkinter import *
root = Tk()
root.title("h")

introText = Label(root, text = "Please enter the following")
introText.grid(row=0, column = 0, columnspan = 2)

firstNameText = Label(root, text = "First Name")
firstNameText.grid(row=1, column = 0)

firstNameEntry = Entry(root)
firstNameEntry.grid(row=1, column = 1)

lastNameText = Label(root, text = "Last Name")
lastNameText.grid(row=2, column = 0)

lastNameEntry = Entry(root)
lastNameEntry.grid(row=2, column = 1)

ageText = Label(root, text = "Age")
ageText.grid(row=3, column = 0)

ageEntry = Entry(root)
ageEntry.grid(row=3, column = 1)

gradeText = Label(root, text = "Grade")
gradeText.grid(row=4, column = 0)

gradeEntry = Entry(root)
gradeEntry.grid(row=4, column = 1)

cityText = Label(root, text = "City")
cityText.grid(row=5, column = 0)

cityEntry = Entry(root)
cityEntry.grid(row=5, column = 1)

def submit():
    firstName = firstNameEntry.get()
    lastName = lastNameEntry.get()
    age = ageEntry.get()
    grade = gradeEntry.get()
    city = cityEntry.get()
    print("First Name:", firstName)
    print("Last Name:", lastName)
    print("Age:", age)
    print("Grade:", grade)
    print("City:", city)
    combinedData = [firstName + "\n", lastName + "\n", age + "\n", grade + "\n", city + "\n"]
    fileVar = open("Tkinter Ex 2 Doc.txt", "w")
    fileVar.writelines(combinedData)
    fileVar.close

submitButton = Button(root, text = "Submit", fg = "blue", command = submit)
submitButton.grid(row=6, column = 0)

def clear():
    firstNameEntry.delete(0, END)
    lastNameEntry.delete(0, END)
    ageEntry.delete(0, END)
    gradeEntry.delete(0, END)
    cityEntry.delete(0, END)

clearButton = Button(root, text = "Clear", fg = "red", command = clear)
clearButton.grid(row=6, column = 1)

root.mainloop()

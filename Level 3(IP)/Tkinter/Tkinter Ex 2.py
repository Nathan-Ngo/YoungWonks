from tkinter import *
root = Tk()
root.title("h")

introText = Label(root, text = "Please enter the following")
introText.pack()

firstNameText = Label(root, text = "First Name")
firstNameText.pack()

firstNameEntry = Entry(root)
firstNameEntry.pack()

lastNameText = Label(root, text = "Last Name")
lastNameText.pack()

lastNameEntry = Entry(root)
lastNameEntry.pack()

ageText = Label(root, text = "Age")
ageText.pack()

ageEntry = Entry(root)
ageEntry.pack()

gradeText = Label(root, text = "Grade")
gradeText.pack()

gradeEntry = Entry(root)
gradeEntry.pack()

cityText = Label(root, text = "City")
cityText.pack()

cityEntry = Entry(root)
cityEntry.pack()

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
submitButton.pack(side = LEFT)

def clear():
    firstNameEntry.delete(0, END)
    lastNameEntry.delete(0, END)
    ageEntry.delete(0, END)
    gradeEntry.delete(0, END)
    cityEntry.delete(0, END)

clearButton = Button(root, text = "Clear", fg = "red", command = clear)
clearButton.pack(side = RIGHT)

root.mainloop()

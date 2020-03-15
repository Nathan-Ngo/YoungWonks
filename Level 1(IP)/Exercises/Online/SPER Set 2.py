#SPER Set 2
#By Nathan Ngo

#1: Write a For Loop to write your name 22 times.

for loop in range(1,23,1):
    print("Nathan")

#2: Write a For Loop to print all the even numbers from 1 to 50.

for loop in range(0,51,2):
    print(loop)

#3: Write a For Loop to print all the odd numbers from 1 to 50.

for loop in range(1,51,2):
    print(loop)

#4: Write a For Loop to print all the multiples of 3 between 1 and 30.

for loop in range(0,31,3):
    print(loop)

#5: Write a program that asks the names of 10 people one by one and prints the following after asking each name:

#Hello {name}

#{name} will be the actual name of the person.

#Example:

#What is your name?

#User's response: Vishal

#Computer's output: Hello Vishal

#What is your name?

#User's response: Suchin

#Computer's output: Hello Suchin

#This should go on for 10 people without running the program again.

for loop in range(1,11,1):
    print("What is your name?")
    name = input()
    print("Hello", name)

#6: Write a program to print the numbers from 50 to 1.

for loop in range(50,0,-1)
    print(loop)

#7: In this program, identify the following:

#How many times will 'I Love YoungWonks' be printed by the program?

#Which variable is the counter variable?

#What is the role of a counter variable?

#Identify start, stop and step in the above program.

#"I love Youngwonks" will be printed 4 times.
#n is the counter variable
#Counter is an interger variable used to keep track of number of times a specific piece of code is executed.
#1 is start, 11 is end, and 2 is step

#8: Use a While Loop to print all numbers from 1 to 50.

x = 0
while x <= 50:
    print(x)
    x = x + 1

#9: Use a While Loop to print numbers from 50 to 01.

x = 50
while x >= 1:
    print(x)
    x = x - 1

#10: Use a While Loop to print multiples of 7 between 1 and 50.
x = 0
while x<=50:
    print(x)
    x = x+7

#11: Use a While Loop to keep asking people's names till the name entered is your name.

while True:
    print("What's your name?")
    name = input()
    if name == "Nathan":
        break

#12: Ask the user the following:

#How many people are working in the farm?

#On an average, how many boxes of strawberries are picked by each farmworker in one day?

#How many strawberries does each box of strawberries contain?

#Once the program has this information, the program should calculate and print the following:

#Number of strawberries picked by one worker in one day is _____ .

#Assuming an 8-hour work day, the average number of strawberries picked by a worker in one hour is _____ .
    
print("How many people are working in the farm?")
answer1 = input()
print("On an average, how many boxes of strawberries are picked by each farmworker in one day?")
answer2 = input()
print("How many strawberries does each box of strawberries contain?")
answer3 = input()
print("Number of strawberries picked by one worker in one day is", answer2 , ".")
answer4 = 8 * answer2
print("Assuming an 8-hour work day, the average number of strawberries picked by a worker in one hour is", answer4 , ".")

#13: Let's assume that a person can work without any restrictions if they are 18 years old or older.

#Those between the ages of 14 and 17 (14 and 17 included) can work only if they have a GPA of 3.5 or above.

#Those below the age of 14 are not allowed to work.

#Write a work eligibility calculator which asks the user their age. If they are between 14 and 17 years of age, it should ask for their GPA.

#Based on the user's answers, the program should print if the person is allowed to work or not.

print("What's your age?")
age = input()
if age >= 14 and age <= 17:
    print("What's your GPA?")
    gpa = int(input())
    if gpa >= 3.5:
        print("You are allowed to work.")
    else:
        print("You are not allowed to work.")
else:
    print("You are not allowed to work.")
    

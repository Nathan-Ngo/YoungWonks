#Youngwonks(SPER) Python Set 2 Answers
#By Nathan Ngo

#Exercise 1: For Loop
for loop_var in range(1,101,1):
    print("name")

#Exercise 2
for loop_a in range(1,101,1):
    print("name", a)

#Exercise 3
for loop_a in range(1,21,1):
    if a%2 == 0:
        print("even")
    else:
        print("odd")

#Exercise 4: Time Module
for loop_a in range(0,5,-1)
    if a == 0:
        print("Blast Off!")
    else:
        print(a)

#Exercise 5
#Unknown! Need answer!

#Exercise 6
#Unknown! Need Answer!

#Exercise 7
for loop_var in range (1,4,1):
    for loop_var in range (1,5,1):
        print('*', end = '')
    print()

#Exercise 8
for loop_x in range(1,5,1):
    for loop_y in range(1,x,1):
        print('x', end ='')
    print()

#Exercise 9: While Loop
x= 0
while x >= 50:
    print(x)
    x = x+1

#Exercise 9a:
x = -120
while x <= 120:
    print(x)
    x = x+1

#Exercise 9b
x = 20
while x >= 0:
    print(x)
    x = x-1
    if x ==0:
        while x <= 35:
            print(x)
            x = x+1

#Exercise 9c
x = -17
while x <= 25:
    print(x)
    x = x+1
    if x == 25:
        while x <= 8:
            print(x)
            x = x-1
    if x == 8:
        print("Bing!")

#Exercise 10: Answer True or False
#Figure it out yourself. uwo

#Exercise 11: if else
a=0
print("What is the price of the item?")
price = int(input())
if price <= 10:
    a = .9
    b = price * .9
    print("Your discount was 10%. Your price is", b,'.')

else:
    a = .8
    c = price * .8
    print("Your discount is 20%. Your price is", c,'.')

#Exercise 12: Logical Operation: and
    print("How old are you?")
    age = input()
    print("What is your grade?")
    grade = input()
    if age >= 8 and grade >= 3:
        print("You are elgible to play the game.")

    else:
        print("You are not elgible to play the game.")

#Exercise 13: Logical Operation: or
print("What state do you live in?")
state  = input()
if state == 'California' or state = 'Oregon' or state = 'Washington':
    print("We suggest you go for a state drive.")
else:
    print("You may be better off skiing.")

#Exercise 14: Logical Operation: not
print("Do you have an upcoming vacation?")
vacation = input()
if vacation == 'yes' or "Yes":
    print("What grade are you in?")
    grade = input()
    if grade != 12:
        print("Have an adventurous vacation.")
    else:
        print("Great time to study for the vacation.")
else:
    print("oh ok")

#Exercise 15: Loops
for x in range (1,101,2):
    print(x)

#Exercise 16
for x in range (100,0,-3):
    if x>20 and x<30:
        print("Tick Tock")
    else:
        print(x)

#Exercise 17:(Tip: Use while)
x = 5
import time
while x > 0
x = x-1
if x == 0:
    time.sleep(1)
    print("Blast Off!")
else:
    print(x)

#Exercise 18
for loop_var in range(0,3,1):
    for loop_var in range(0,3,1):
        for loop_var in range(0,7,1):
            print('*', end='')
        print()
    print()

#Exercise 19(Printed as Exercise 18): random module
import random
a = random.randint(1,10)

import random
random.random()

#Exercise 20(Printed as Exercise 19)
import random
import time
while True:
    time.sleep(3)
    a = random.random()
    num = random.randint(0.1,10)
    print(a)
    print(num)

#Exercise 21(Printed as Exercise 20)
import random
Total = 0
for loop_y in range(0,21,1):
    x = random.randint(0,20)
    Total = Total + x
if y = 20:
    Total = Total/20
print(Total)

#Exercise 22(Printed as Exercise 21)
import random
Total = 0
for loop_b in range(0,21,1):
    a = random.randint(-20,20)
    Total = Total + a
if b == 20:

#Only beginning of code, doesn't work unless you know lists

#Mini Project: Rolling Dice Mini Project

import time
import random
x = 0
print("How much money would you like to deposit to your account?")
money = input()
while True:
    if money < 0:
        print("You ran out of money....")
    print("Would you like rolling dice or not?")
    choice = input()
    if Variable2 = "No" or Variable2 = "n" or Variable2 = "N":
        print("You have quitted the game.")
        break
    if Variable2 = "Yes" ir Variable2 = "y" or Variable2 = "Y":
        print("Alright. Waiting a few seconds....")
        time.sleep(2)
        Variable3 = random.randint(1,6)
        Variable4 = random.randint(1,6)
        print(Variable3, Variable4)
        if Variable3 == Variable4:
            print("You win!")
            money = money + 5
        else:
            print("You lose.")
            money = money - 1
        print("You have", money, "dollars left.")
    
    


    
        
    
    
    
        


    
        
        
        

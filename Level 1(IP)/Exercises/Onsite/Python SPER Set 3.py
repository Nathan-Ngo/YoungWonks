#YoungWonks Python(SPER) Set 3 Answers
#By Nathan Ngo

#Exercise 1: Creating a List
friends = ["Ethan C.", "Andy", "Jerry", "Tony", "Justin"]

#Exercise 2
friends = ["Ethan C.", "Andy", "Jerry", "Tony", "Justin"]
print(len(friends))

#Exercise 3
friends = ["Ethan C.", "Andy", "Jerry", "Tony", "Justin"]
print(friends[1])

#Exercise 4
friends = ["Ethan C.", "Andy", "Jerry", "Tony", "Justin"]
print(friends[1:3])

#Exercise 5
friends = ["Ethan C.", "Andy", "Jerry", "Tony", "Justin"]
friends[0] = "Trinitzing"
print(friends)

#Exercise 6: Insert Method
friends = ["Ethan C.", "Andy", "Jerry", "Tony", "Justin"]
friends.insert(3,"Potato")
print(friends)

#Exercise 7: Append Method(add to the end)
friends = ["Ethan C.", "Andy", "Jerry", "Tony", "Justin"]
friends.append("Phil Swift")

#Exercise 8: Pop Method(remove by index)
friends = ["Ethan C.", "Andy", "Jerry", "Tony", "Justin"]
friensd.pop(1)
print(friends)

#Exercise 9: Remove Method(remove by value)
friends = ["Ethan C.", "Andy", "Jerry", "Tony", "Justin"]
friends.remove("Andy")
print(friends)

#Exercise 10: Methods that Return a value
friends = ["Ethan C.", "Andy", "Jerry", "Tony", "Justin"]
t = friends.pop(2)
print(t)

#Exercise 11: Sort Method
friends = ["Ethan C.", "Andy", "Jerry", "Tony", "Justin"]
buddies = friends.sort()
mates = buddies.sort(reverse = True)
print(buddies)
print(mates)

#Exercise 12: Split and Join Methods
a = StringVar("Hello, how are you string")
b = a.split()

c = StringVar("Hello, how are you?")
d = list(c)

''.join(d)

#Exercise 13: Password Check
print("Enter the codename:")
codename = input()
while True:
    if codename == 'Oliver':
        print("Access granted.")
        break
    else:
        print("Access denied.")

#Exercise 14
tries = []
while True:
    print("Enter the codename:")
    codename = input()
    if codename == 'Oliver':
        print("Access granted. Wrong Passwords Tried:", tries,'.')
        break
    else:
        print("Access denied.")
        tries.append()

#Exercise 15
tries = []
while True:
    print("Enter the codename:")
    codename = input()
    if codename == 'Oliver' or codename = ' ':
        print("Access granted. Wrong Passwords Tried:", tries,'.')
        break
    else:
        print("Access denied.")
        tries.append()

#Exercise 16: Random Lists
import random
numbers = []
for loop_var in range(1,21,1):
    a = randomr.randint(1,50)
    numbers.append(a)
    a.sort()
print(a[0])
print(a[19]

#Exercise 17
a = ["Mickey", "Minnie", "Pluto", "Donald Duck", "Elmer Fudd", "Big Chungus", "Spongebob", "Squidward", "Mr. Krabs"]
#a can be anything, just make sure they're all cartoon characters
for loop_var in range(1,11,1):
      random.shuffle(a)
print(a[0])

#Exercise 18
a = ["Mickey", "Minnie", "Pluto", "Donald Duck", "Elmer Fudd", "Big Chungus", "Spongebob", "Squidward", "Mr. Krabs"]
b = random.choice(a)
print(b)
c = random.sample(a,3)
print(c)

#Exercise 19: Convert String To List
list("string")

#Exercise 20: in keyword
#True Scenario:
a = ['oh','reee','this list could have anything in it']
'a' in a

#False Scenario:
b = 'oh'
c in b

#Exercise 21: Looping/iterating over a list of string
a = ['despacito', 'noice', 'egg']
b = 'boi'
for b in a:
    print(a)

#Project: Lists and Random Mini Project
memes = ['lemon car', 'boi','reverse card', 'stalin', 'noice', 'fbi open up', 'meem']
a = random.choice(memes)
b = list(a)      
    
    

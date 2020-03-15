#SPER Set 3
#By Nathan Ngo

#1: Make a list of 6 fruits that you might have at home.

fruits = ["apple", "longan", "banana", "orange", "blueberry", "grape"]

#2: Now assume that you have decided to eat the fruit that forms the last element on the list. Remove the last element from the list.

fruits = ["apple", "longan", "banana", "orange", "blueberry", "grape"]
fruits.pop()

#3: Now let's assume you have a special fruit that you want to eat only when all your other fruits have been eaten, so you want to add this fruit to the end of the list. Make sure you DO NOT USE the insert method.

fruits = ["apple", "longan", "banana", "orange", "blueberry", "grape"]
fruits.append("the special fruit")

#4: Let's assume you have started eating your fruits and have eaten the third fruit. Remove that fruit from the list.

#You need to use the element number to remove and not the name of the fruit.

fruits = ["apple", "longan", "banana", "orange", "blueberry", "grape"]
fruits.pop(2)

#5: Let's assume you eat another of your fruits. This will again be the new third element. Remove that fruit from the list.

#You need to use the element number to remove and not the name of the fruit.

fruits = ["apple", "longan", "banana", "orange", "blueberry", "grape"]
fruits.pop(2)
fruits.pop(2)

#6: Now let's assume you bought one more fruit; now insert that fruit in the list. Make sure that the new inserted element IS NOT the last element on the list.

fruits = ["apple", "longan", "banana", "orange", "blueberry", "grape"]
fruits.pop(2)
fruits.pop(2)
fruits.insert(2, "green grapes")

#7: Now add apple to the end of your list.

fruits = ["apple", "longan", "banana", "orange", "blueberry", "grape"]
fruits.pop(2)
fruits.pop(2)
fruits.insert(2, "green grapes")
fruits.append("apple 2")

#8: Remove apple using the the name of the element, 'apple'.

#The index of the element should not be used.

fruits = ["apple", "longan", "banana", "orange", "blueberry", "grape"]
fruits.pop(2)
fruits.pop(2)
fruits.insert(2, "green grapes")
fruits.append("apple 2")
fruits.remove("apple 2")

#9: Using For Loop, print each element of the list. Each fruit should be printed on a different line.

fruits = ["apple", "longan", "banana", "orange", "blueberry", "grape"]
for loop in range(0,5,1):
    print(fruits[loop])

#10: Make a dictionary of 5 movies you have watched. The movie name will be the key of the dictionary and enter your movie rating (a number between 1 and 5) as the value of the dictionary.

#Do not delete your dictionary; subsequent questions are a continuation of this exercise.

movies = {"killer bean": "5", "frozen": "1", "Avatar": "4", "Avengers: Infinity War": "5", "Bumblebee": "5"}

#11: Take the dictionary from the previous exercise and using the for loop, print all the keys of the dictionary.

#Do not delete your dictionary; subsequent questions are a continuation of this exercise.

movies = {"killer bean": "5", "frozen": "1", "Avatar": "4", "Avengers: Infinity War": "5", "Bumblebee": "5"}
for loop in range(0,5,1):
    print(movies.keys())

#12: Take the dictionary from the previous exercise and using the for loop, print all the keys and the values of the dictionary.

#The output should read like this:
    #Movie Name    Rating: 5
    #Movie Name    Rating: 3
    #Movie Name    Rating: 2

movies = {"killer bean": "5", "frozen": "1", "Avatar": "4", "Avengers: Infinity War": "5", "Bumblebee": "5"}
for loop in range(0,5,1):
    print(movies.keys(), movies.values())

#13: Take the dictionary from the previous exercise and using the For Loop and If condition, print only those movies that have a rating greater than 3.

#The output should be like this:


#Movie Name    Rating: 5
#Movie Name    Rating: 3

movies = {"killer bean": 5, "frozen": 1, "Avatar": 4, "Avengers: Infinity War": 5, "Bumblebee": 5}
for loop in range(0,5,1):
    if movies[loop] >= 3:
        print(movies.keys[loop], "Rating:", movies.values[loop])

#14: Using for loop, print each element of your name (each letter) in a separate line.
s = "Nathan"
list(s)
for loop in range(0,6,1):
    print(s[loop])
    
